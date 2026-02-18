#!/usr/bin/env python3
"""
Scan Maildir for academically significant emails and generate Hugo news posts.

Uses local Ollama AI to classify emails as newsworthy based on:
- Paper acceptances, awards, grants
- Conference invitations, keynotes
- Project milestones, collaborations
- Academic appointments, visits

Usage:
    # Scan last 30 days (default):
    python3 scripts/scrape_news.py

    # Scan last 90 days:
    python3 scripts/scrape_news.py --days 90

    # Dry run (classify but don't create posts):
    python3 scripts/scrape_news.py --dry-run

    # Scan specific date range:
    python3 scripts/scrape_news.py --after 2025-01-01 --before 2025-06-01

    # Use a different Ollama model:
    python3 scripts/scrape_news.py --model mistral
"""

import argparse
import email
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from email.header import decode_header
from email.utils import parsedate_to_datetime
from pathlib import Path
from textwrap import dedent

OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "llama3.1:latest"

MAILDIR = Path.home() / "Maildir"
SITE_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = SITE_ROOT / "content" / "post"

# Skip emails from these senders (mailing lists, newsletters, etc.)
SKIP_SENDERS = [
    "noreply", "no-reply", "mailer-daemon", "notifications",
    "newsletter", "digest", "marketing", "promo",
    "info@email.sagepub.com", "news@nvidia.com",
    "events@mentorhellas.com",
    "vlaxose@upatras.gr",
]

# Only process emails mentioning these academic keywords (pre-filter)
KEYWORD_HINTS = [
    "accept", "award", "grant", "fund", "paper", "publish", "journal",
    "conference", "invited", "keynote", "project", "collaborat",
    "visit", "appointment", "tenure", "position", "review",
    "horizon", "proposal", "ieee", "submission", "camera-ready",
    "congratul", "milestone", "kick-off", "kickoff", "launch",
    "patent", "fellowship", "scholarship", "phd", "postdoc",
]


def decode_mime_header(header_value):
    """Decode a MIME-encoded header into a plain string."""
    if not header_value:
        return ""
    parts = decode_header(header_value)
    decoded = []
    for data, charset in parts:
        if isinstance(data, bytes):
            decoded.append(data.decode(charset or "utf-8", errors="replace"))
        else:
            decoded.append(data)
    return " ".join(decoded)


def extract_text_body(msg):
    """Extract plain text body from an email message."""
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            if ctype == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    charset = part.get_content_charset() or "utf-8"
                    body += payload.decode(charset, errors="replace")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            charset = msg.get_content_charset() or "utf-8"
            body = payload.decode(charset, errors="replace")
    return body[:3000]  # Truncate to save tokens


def parse_maildir(maildir_path, after_date, before_date):
    """Read emails from Maildir and return filtered list."""
    emails = []
    seen_msgids = set()
    seen_subjects = set()
    for subdir in ["new", "cur"]:
        dirpath = maildir_path / subdir
        if not dirpath.exists():
            continue
        for fname in os.listdir(dirpath):
            fpath = dirpath / fname
            try:
                with open(fpath, "rb") as f:
                    msg = email.message_from_binary_file(f)

                # Deduplicate by Message-ID
                msgid = msg.get("Message-ID", "").strip()
                if msgid and msgid in seen_msgids:
                    continue
                if msgid:
                    seen_msgids.add(msgid)

                # Parse date
                date_str = msg["Date"]
                if not date_str:
                    continue
                try:
                    dt = parsedate_to_datetime(date_str)
                except Exception:
                    continue

                # Make timezone-aware for comparison
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)

                if dt < after_date or dt > before_date:
                    continue

                sender = decode_mime_header(msg["From"]).lower()
                if any(skip in sender for skip in SKIP_SENDERS):
                    continue

                subject = decode_mime_header(msg["Subject"])

                # Deduplicate by subject + date (catches duplicates without Message-ID)
                dedup_key = (subject.strip().lower(), dt.date())
                if dedup_key in seen_subjects:
                    continue
                seen_subjects.add(dedup_key)

                body = extract_text_body(msg)
                combined = (subject + " " + body).lower()

                # Pre-filter: must contain at least one keyword hint
                if not any(kw in combined for kw in KEYWORD_HINTS):
                    continue

                emails.append({
                    "date": dt,
                    "from": decode_mime_header(msg["From"]),
                    "subject": subject,
                    "body": body,
                })
            except Exception:
                continue

    # Sort by date descending
    emails.sort(key=lambda e: e["date"], reverse=True)
    return emails


def ollama_chat(model, prompt, retries=2):
    """Send a prompt to local Ollama and return the response text."""
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.1},
    }).encode("utf-8")

    for attempt in range(retries + 1):
        req = urllib.request.Request(
            OLLAMA_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                return result["message"]["content"]
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < retries:
                print(f"  Ollama request failed ({e}), retrying ({attempt + 1}/{retries})...")
                continue
            print(f"Error connecting to Ollama at {OLLAMA_URL}: {e}")
            print("Make sure Ollama is running: ollama serve")
            sys.exit(1)


def classify_batch(model, emails_batch):
    """Send a batch of emails to Ollama for classification."""
    email_summaries = []
    for i, em in enumerate(emails_batch):
        email_summaries.append(
            f"--- EMAIL {i+1} ---\n"
            f"Date: {em['date'].strftime('%Y-%m-%d')}\n"
            f"From: {em['from']}\n"
            f"Subject: {em['subject']}\n"
            f"Body (excerpt): {em['body'][:1500]}\n"
        )

    prompt = dedent(f"""\
    You are an assistant for Dr. Evangelos Vlachos, a researcher at the Industrial
    Systems Institute (ISI), Athena RC, Greece. His email addresses are:
    evlachos@athenarc.gr, vlachose@upatras.gr, vlachos.evangelos@gmail.com.
    His research areas: Joint Communication and Sensing, ISAC, 6G, UAV swarms,
    signal processing, deep unfolding.

    Below are {len(emails_batch)} emails from his mailbox. Classify each as either
    NEWSWORTHY or SKIP.

    An email is NEWSWORTHY only if it **directly involves** Dr. Vlachos and relates to:
    - Paper acceptance at a journal or conference
    - Awards, best paper prizes
    - Grant/project funding decisions (accepted proposals)
    - Project milestones, kick-off meetings for his projects
    - Invited talks, keynotes, panels he is involved in
    - Academic appointments, visiting positions
    - Major collaborations starting
    - PhD defenses, graduations of supervised students

    SKIP emails that are:
    - Routine correspondence, meeting scheduling
    - Generic call for papers or award nomination calls
    - Peer review requests
    - Administrative/bureaucratic emails
    - University-wide or department-wide announcements not specifically about Dr. Vlachos
    - Newsletters, promotional emails, mailing list digests
    - Events or seminars he is not presenting at

    For each NEWSWORTHY email, provide:
    - title: A concise news title (max 80 chars)
    - summary: A 1-2 sentence summary for the website
    - tags: Comma-separated relevant tags from: research, award, grant, horizon-europe, 6g, uavs, isac, deep-learning, collaboration, appointment

    Respond ONLY in this exact format for each email (no extra text):

    EMAIL <number>: NEWSWORTHY
    title: <title>
    summary: <summary>
    tags: <tags>

    or

    EMAIL <number>: SKIP

    Here are the emails:

    {"".join(email_summaries)}
    """)

    return ollama_chat(model, prompt)


def parse_classifications(response_text, emails_batch):
    """Parse AI classification response."""
    newsworthy = []
    lines = response_text.strip().split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        match = re.match(r"EMAIL\s+(\d+):\s*(NEWSWORTHY|SKIP)", line, re.IGNORECASE)
        if match:
            idx = int(match.group(1)) - 1
            status = match.group(2).upper()
            if status == "NEWSWORTHY" and 0 <= idx < len(emails_batch):
                title = summary = ""
                tags = []
                for j in range(i + 1, min(i + 4, len(lines))):
                    l = lines[j].strip()
                    if l.lower().startswith("title:"):
                        title = l[6:].strip().strip('"')
                    elif l.lower().startswith("summary:"):
                        summary = l[8:].strip().strip('"')
                    elif l.lower().startswith("tags:"):
                        tags = [t.strip() for t in l[5:].split(",") if t.strip()]
                newsworthy.append({
                    "email": emails_batch[idx],
                    "title": title,
                    "summary": summary,
                    "tags": tags,
                })
        i += 1
    return newsworthy


def slugify(text):
    """Create a URL-friendly slug from text."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:60].rstrip("-")


def create_post(item, dry_run=False):
    """Create a Hugo post from a classified news item."""
    date = item["email"]["date"].strftime("%Y-%m-%d")
    slug = slugify(item["title"])
    post_dir = POSTS_DIR / slug

    if post_dir.exists():
        print(f"  [exists] {slug}")
        return False

    tags_yaml = "\n".join(f'  - {t}' for t in item["tags"]) if item["tags"] else '  - research'
    content = dedent(f"""\
    ---
    title: "{item['title']}"
    date: {date}
    summary: "{item['summary']}"
    tags:
    {tags_yaml}
    ---

    {item['summary']}
    """)

    if dry_run:
        print(f"  [dry-run] Would create: {slug}/index.md")
        print(f"    Title: {item['title']}")
        print(f"    Date: {date}")
        print(f"    Summary: {item['summary']}")
        return True

    post_dir.mkdir(parents=True, exist_ok=True)
    (post_dir / "index.md").write_text(content)
    print(f"  [created] {slug}/index.md")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Scan Maildir for newsworthy emails and create Hugo posts"
    )
    parser.add_argument(
        "--days", type=int, default=30,
        help="Scan emails from the last N days (default: 30)"
    )
    parser.add_argument(
        "--after", type=str, default=None,
        help="Only emails after this date (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--before", type=str, default=None,
        help="Only emails before this date (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Classify emails but don't create posts"
    )
    parser.add_argument(
        "--batch-size", type=int, default=10,
        help="Number of emails per AI classification batch (default: 10)"
    )
    parser.add_argument(
        "--model", type=str, default=DEFAULT_MODEL,
        help=f"Ollama model to use (default: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--maildir", type=str, default=str(MAILDIR),
        help=f"Path to Maildir (default: {MAILDIR})"
    )
    args = parser.parse_args()

    # Check Ollama is reachable
    try:
        urllib.request.urlopen(
            "http://localhost:11434/api/tags", timeout=5
        )
    except Exception:
        print("Error: Cannot connect to Ollama at localhost:11434")
        print("Make sure Ollama is running: ollama serve")
        sys.exit(1)

    # Date range
    now = datetime.now(timezone.utc)
    if args.after:
        after_date = datetime.strptime(args.after, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    else:
        after_date = now - timedelta(days=args.days)

    if args.before:
        before_date = datetime.strptime(args.before, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    else:
        before_date = now

    maildir_path = Path(args.maildir)
    print(f"Using Ollama model: {args.model}")
    print(f"Scanning {maildir_path} for emails from {after_date.date()} to {before_date.date()}...")

    # Step 1: Read and pre-filter emails
    emails = parse_maildir(maildir_path, after_date, before_date)
    print(f"Found {len(emails)} emails matching keyword filters.")

    if not emails:
        print("No candidate emails found.")
        return

    # Step 2: Classify with AI in batches
    all_newsworthy = []

    for batch_start in range(0, len(emails), args.batch_size):
        batch = emails[batch_start:batch_start + args.batch_size]
        batch_num = batch_start // args.batch_size + 1
        total_batches = (len(emails) + args.batch_size - 1) // args.batch_size
        print(f"\nClassifying batch {batch_num}/{total_batches} ({len(batch)} emails)...")

        response = classify_batch(args.model, batch)
        newsworthy = parse_classifications(response, batch)
        all_newsworthy.extend(newsworthy)
        print(f"  Found {len(newsworthy)} newsworthy items in this batch.")

    print(f"\n{'='*60}")
    print(f"Total newsworthy emails: {len(all_newsworthy)}")
    print(f"{'='*60}\n")

    if not all_newsworthy:
        print("No newsworthy emails found.")
        return

    # Step 3: Create Hugo posts
    created = 0
    for item in all_newsworthy:
        if create_post(item, dry_run=args.dry_run):
            created += 1

    action = "Would create" if args.dry_run else "Created"
    print(f"\n{action} {created} new post(s) in {POSTS_DIR}")


if __name__ == "__main__":
    main()
