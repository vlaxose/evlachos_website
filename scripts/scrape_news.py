#!/usr/bin/env python3
"""
Scan Maildir for academically significant emails and generate Hugo news posts.
Includes support for Greek academic terms and internship postings.
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

# Skip emails from these senders
SKIP_SENDERS = [
    "noreply", "no-reply", "mailer-daemon", "notifications",
    "newsletter", "digest", "marketing", "promo",
    "info@email.sagepub.com", "news@nvidia.com",
    "events@mentorhellas.com",
    "vlaxose@upatras.gr",
]

# --- MULTILINGUAL KEYWORDS ---
KEYWORD_HINTS = [
    # English
    "accept", "award", "grant", "fund", "paper", "publish", "journal",
    "conference", "invited", "keynote", "project", "collaborat",
    "visit", "appointment", "tenure", "position", "review",
    "horizon", "proposal", "ieee", "submission", "camera-ready",
    "congratul", "milestone", "kick-off", "launch", "internship",
    "patent", "fellowship", "scholarship", "phd", "postdoc", "opening",
    # Greek
    "αποδοχή", "βραβείο", "χρηματοδότηση", "δημοσίευση", "περιοδικό",
    "συνέδριο", "πρόσκληση", "έργο", "συνεργασία", "επίσκεψη",
    "θέση", "αξιολόγηση", "πρόταση", "υποβολή", "πρακτική", 
    "υποτροφία", "διδακτορ", "μεταδιδακτορ", "προκήρυξη", "ανακοίνωση"
]

def normalize_text(text):
    """Normalize Greek accents and lowercase for robust matching."""
    if not text: return ""
    accents = str.maketrans("άέήίόύώϊϋΐΰ", "αεηιουωιυιυ")
    return text.lower().translate(accents)

def decode_mime_header(header_value):
    if not header_value: return ""
    parts = decode_header(header_value)
    decoded = []
    for data, charset in parts:
        if isinstance(data, bytes):
            decoded.append(data.decode(charset or "utf-8", errors="replace"))
        else:
            decoded.append(data)
    return " ".join(decoded)

def extract_text_body(msg):
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
    return body[:3000]

def parse_maildir(maildir_path, after_date, before_date):
    emails = []
    seen_msgids = set()
    seen_subjects = set()
    
    for subdir in ["new", "cur"]:
        dirpath = maildir_path / subdir
        if not dirpath.exists(): continue
        for fname in os.listdir(dirpath):
            fpath = dirpath / fname
            try:
                with open(fpath, "rb") as f:
                    msg = email.message_from_binary_file(f)

                msgid = msg.get("Message-ID", "").strip()
                if msgid and msgid in seen_msgids: continue
                if msgid: seen_msgids.add(msgid)

                date_str = msg["Date"]
                if not date_str: continue
                dt = parsedate_to_datetime(date_str)
                if dt.tzinfo is None: dt = dt.replace(tzinfo=timezone.utc)

                if dt < after_date or dt > before_date: continue

                sender = decode_mime_header(msg["From"]).lower()
                if any(skip in sender for skip in SKIP_SENDERS): continue

                subject = decode_mime_header(msg["Subject"])
                dedup_key = (subject.strip().lower(), dt.date())
                if dedup_key in seen_subjects: continue
                seen_subjects.add(dedup_key)

                body = extract_text_body(msg)
                
                # Pre-filter using normalized Greek/English text
                combined_normalized = normalize_text(subject + " " + body)
                if not any(kw in combined_normalized for kw in KEYWORD_HINTS):
                    continue

                emails.append({
                    "date": dt,
                    "from": decode_mime_header(msg["From"]),
                    "subject": subject,
                    "body": body,
                })
            except Exception: continue

    emails.sort(key=lambda e: e["date"], reverse=True)
    return emails

def ollama_chat(model, prompt, retries=2):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.1},
    }).encode("utf-8")

    for attempt in range(retries + 1):
        req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                return result["message"]["content"]
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < retries: continue
            print(f"Error connecting to Ollama: {e}")
            sys.exit(1)

def classify_batch(model, emails_batch):
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
    You are an assistant for Dr. Evangelos Vlachos (ISI, Athena RC). 
    Your goal is to identify and translate emails for his website news section.

    Classify these {len(emails_batch)} emails as NEWSWORTHY or SKIP.

    NEWSWORTHY if:
    - Paper accepted, awards, or project funding.
    - Invited talks, keynotes, or workshop chairing.
    - LAB OPPORTUNITIES: Calls for internship positions, PhDs, or PostDocs in his team.
    - Milestones like project kick-offs or new major industrial collaborations.

    SKIP if:
    - Generic Call for Papers (CFPs) he didn't submit to.
    - Routine administrative updates or meeting scheduling.
    - Newsletters or mailing list digests.

    CRITICAL: 
    If the email is in Greek, you MUST translate the 'title' and 'summary' into professional ENGLISH.

    Respond ONLY in this format:
    EMAIL <number>: NEWSWORTHY
    title: <English Title>
    summary: <English Summary>
    tags: <comma separated tags>

    or
    EMAIL <number>: SKIP

    Emails:
    {"".join(email_summaries)}
    """)

    return ollama_chat(model, prompt)

def parse_classifications(response_text, emails_batch):
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
                for j in range(i + 1, min(i + 6, len(lines))):
                    l = lines[j].strip()
                    if l.lower().startswith("title:"): title = l[6:].strip().strip('"')
                    elif l.lower().startswith("summary:"): summary = l[8:].strip().strip('"')
                    elif l.lower().startswith("tags:"): tags = [t.strip() for t in l[5:].split(",") if t.strip()]
                newsworthy.append({
                    "email": emails_batch[idx],
                    "title": title,
                    "summary": summary,
                    "tags": tags,
                })
        i += 1
    return newsworthy

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:60].rstrip("-")

def create_post(item, dry_run=False):
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
        print(f"  [dry-run] Would create: {slug}/index.md | Title: {item['title']}")
        return True

    post_dir.mkdir(parents=True, exist_ok=True)
    (post_dir / "index.md").write_text(content)
    print(f"  [created] {slug}/index.md")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--after", type=str)
    parser.add_argument("--before", type=str)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL)
    parser.add_argument("--maildir", type=str, default=str(MAILDIR))
    args = parser.parse_args()

    # Date range setup
    now = datetime.now(timezone.utc)
    after_date = datetime.strptime(args.after, "%Y-%m-%d").replace(tzinfo=timezone.utc) if args.after else now - timedelta(days=args.days)
    before_date = datetime.strptime(args.before, "%Y-%m-%d").replace(tzinfo=timezone.utc) if args.before else now

    maildir_path = Path(args.maildir)
    print(f"Scanning {maildir_path} from {after_date.date()} to {before_date.date()}...")

    emails = parse_maildir(maildir_path, after_date, before_date)
    print(f"Found {len(emails)} candidate emails.")

    if not emails: return

    all_newsworthy = []
    for b in range(0, len(emails), args.batch_size):
        batch = emails[b:b + args.batch_size]
        print(f"Classifying batch {b//args.batch_size + 1}...")
        response = classify_batch(args.model, batch)
        all_newsworthy.extend(parse_classifications(response, batch))

    created = sum(1 for item in all_newsworthy if create_post(item, dry_run=args.dry_run))
    print(f"\nFinished. Processed {created} post(s).")

if __name__ == "__main__":
    main()
