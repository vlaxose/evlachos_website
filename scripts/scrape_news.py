#!/usr/bin/env python3
"""
Smart Academic News Scanner for Dr. Evangelos Vlachos
Scans Maildir for professional emails and uses DeepSeek-R1 (via Ollama)
to identify newsworthy items for the website's news section.
"""
import argparse
import email
import hashlib
import html
import json
import logging
import os
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from email.header import decode_header
from email.utils import parsedate_to_datetime
from pathlib import Path
from textwrap import dedent

# ──────────────────────────────────────────────
# CONFIGURATION — adjust these to your setup
# ──────────────────────────────────────────────
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1:8b"

MAILDIR = Path.home() / "Maildir"

# Hugo site paths
SITE_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = SITE_ROOT / "content" / "post"

# Your email address (lowercased for matching)
MY_EMAILS = [
    "evlachos@athenarc.gr",
]

# Identity tokens — checked in From/To/CC/Delivered-To headers
IDENTITY_TOKENS = ["evlachos@athenarc.gr"]

# Greek + English keywords that hint at professional/academic relevance.
# Checked in subject AND body so we catch mailing-list emails too.
KEYWORDS_SUBJECT = [
    # Greek — Internships / Practical Training (high priority)
    "πρακτική", "άσκηση", "άσκησης", "πρακτικ", "θέση", "θέσεις",
    "προκήρυξη", "αγγελία", "intern",
    # Greek — Academic
    "διδασκαλία", "μεταπτυχιακ",
    "διδακτορ", "ερευνητ", "δημοσίευ", "συνέδρι", "βραβεί",
    "πρόσκληση", "υποτροφ", "χρηματοδότηση", "πρόγραμμα",
    "αποτελέσμ", "εκλογ", "διοικητικ", "συμβούλι",
    "επιτροπ", "πανεπιστημ",
    # English
    "paper", "conference", "journal", "award", "grant", "publication",
    "invited", "keynote", "review", "accepted", "submitted",
    "defense", "thesis", "phd", "proposal", "horizon",
    "erasmus", "internship", "fellowship", "position", "opening",
    "postdoc", "vacancy", "call for",
    # Project-specific
    "isac", "6g", "uav", "swarm",
    # Administrative
    "board", "meeting", "δσ", "δ.σ.",
]

KEYWORDS_BODY = [
    # Only the strongest signals — we don't want to AI-evaluate every email
    "paper accepted", "paper published", "best paper",
    "grant awarded", "project kick-off", "kick off",
    "keynote", "invited talk", "invited speaker",
    "election", "elected", "appointed",
    "εγκρίθηκε", "δημοσιεύτηκε", "βραβείο",
    "πρακτική άσκηση", "πρακτική", "θέση εργασίας",
    "internship position", "intern position", "open position",
    "call for applications", "θέσεις πρακτικής",
]

# Folders to skip entirely
SKIP_FOLDERS = {"junk", "trash", "spam", "drafts", "sent", ".sent", ".trash", ".junk", ".spam", ".drafts"}

# State file to avoid re-processing
STATE_FILE = Path(__file__).resolve().parent / ".scanner_state.json"

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("mail_scanner")


# ──────────────────────────────────────────────
# UTILITIES
# ──────────────────────────────────────────────

def decode_mime_header(header_value):
    """Robustly decode a MIME-encoded header (Subject, From, To, etc.)."""
    if not header_value:
        return ""
    try:
        parts = decode_header(header_value)
        decoded = []
        for data, encoding in parts:
            if isinstance(data, bytes):
                for enc in [encoding, "utf-8", "iso-8859-7", "windows-1253", "latin-1"]:
                    if enc and enc.lower() != "unknown-8bit":
                        try:
                            decoded.append(data.decode(enc))
                            break
                        except (UnicodeDecodeError, LookupError):
                            continue
                else:
                    decoded.append(data.decode("utf-8", errors="replace"))
            else:
                decoded.append(str(data))
        return " ".join(decoded)
    except Exception:
        return str(header_value)


def extract_body(msg):
    """Extract plain-text body from a MIME message; fall back to stripping HTML."""
    text_parts = []
    html_parts = []

    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            # Skip attachments
            if part.get_content_disposition() == "attachment":
                continue
            payload = part.get_payload(decode=True)
            if not payload:
                continue
            charset = part.get_content_charset() or "utf-8"
            try:
                text = payload.decode(charset, errors="replace")
            except (LookupError, UnicodeDecodeError):
                text = payload.decode("utf-8", errors="replace")

            if ctype == "text/plain":
                text_parts.append(text)
            elif ctype == "text/html":
                html_parts.append(text)
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            charset = msg.get_content_charset() or "utf-8"
            try:
                text = payload.decode(charset, errors="replace")
            except (LookupError, UnicodeDecodeError):
                text = payload.decode("utf-8", errors="replace")
            if msg.get_content_type() == "text/html":
                html_parts.append(text)
            else:
                text_parts.append(text)

    # Prefer plain text
    if text_parts:
        return "\n".join(text_parts)

    # Fall back to HTML → plain text
    if html_parts:
        raw = "\n".join(html_parts)
        # Strip tags
        raw = re.sub(r"<style[^>]*>.*?</style>", "", raw, flags=re.DOTALL | re.IGNORECASE)
        raw = re.sub(r"<script[^>]*>.*?</script>", "", raw, flags=re.DOTALL | re.IGNORECASE)
        raw = re.sub(r"<br\s*/?>", "\n", raw, flags=re.IGNORECASE)
        raw = re.sub(r"</?p[^>]*>", "\n", raw, flags=re.IGNORECASE)
        raw = re.sub(r"<[^>]+>", "", raw)
        raw = html.unescape(raw)
        # Collapse whitespace
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip()

    return ""


def get_all_recipients(msg):
    """Return a single lowercased string with all recipient-related headers."""
    fields = []
    for hdr in ["To", "Cc", "Bcc", "Delivered-To", "X-Original-To", "X-Forwarded-To"]:
        val = msg.get_all(hdr) or []
        for v in val:
            fields.append(decode_mime_header(v).lower())
    return " ".join(fields)


def message_id_hash(msg):
    """Return a short hash to de-duplicate messages."""
    mid = msg.get("Message-ID", "")
    if mid:
        return hashlib.sha256(mid.encode()).hexdigest()[:16]
    # Fallback: hash subject + date + from
    blob = f"{msg.get('Subject','')}{msg.get('Date','')}{msg.get('From','')}".encode()
    return hashlib.sha256(blob).hexdigest()[:16]


# ──────────────────────────────────────────────
# AI EVALUATION (DeepSeek-R1 via Ollama)
# ──────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are a news assistant for Dr. Evangelos Vlachos, a researcher at ATHENA Research Center \
and the University of Patras, Greece. His fields include wireless communications, signal processing, \
6G, UAVs, machine learning for communications, and ISAC (Integrated Sensing and Communication).

Your job: decide if an email describes something **newsworthy** for his professional website's \
"News" section.

═══ NEWSWORTHY (mark as true) ═══
  • Paper accepted / published in a journal or conference
  • Award, distinction, or best-paper prize
  • New funded project or grant (EU Horizon, national, etc.)
  • Invited talk, keynote, or panel participation
  • PhD / MSc defense or graduation of a student he supervises
  • Appointment, election, or board meeting (e.g. ΔΣ / Board of Directors)
  • Internship positions / Πρακτική Άσκηση — ANY posting, announcement, call for interns, \
    or update about internship/practical training positions. These are ALWAYS newsworthy.
  • Open positions: job postings, research assistant calls, postdoc openings
  • Major event organisation (conference, workshop, summer school)
  • Collaboration announcements, MoUs, new partnerships

═══ NOT NEWSWORTHY (mark as false) ═══
  • Routine admin (password resets, IT maintenance, room bookings)
  • Spam or marketing
  • Newsletter digests with no specific item about him
  • General university announcements that don't involve his group or field
  • Social/holiday greetings
  • Mailing-list noise unrelated to his work

═══ CRITICAL RULES — DO NOT HALLUCINATE ═══
  • Your title and summary MUST be based ONLY on what is explicitly written in the email.
  • Do NOT invent, assume, or embellish any facts not present in the email text.
  • Do NOT fabricate awards, rankings, recognitions, or achievements.
  • If the email is in Greek, translate what it actually says — do not guess.
  • The "evidence" field must contain a direct quote (copy-paste) from the email that \
    supports your classification. If you cannot find a direct quote, set newsworthy to false.
  • If you are unsure what the email is about, set newsworthy to false.

Respond ONLY with a JSON object (no extra text):
{
  "newsworthy": true/false,
  "confidence": 0.0-1.0,
  "category": "paper|award|grant|talk|defense|appointment|internship|position|event|other",
  "title": "Short English title — MUST reflect actual email content",
  "summary": "2-3 sentence English summary — ONLY facts from the email, nothing invented",
  "evidence": "Direct quote from the email that supports this classification",
  "tags": ["relevant", "tags"]
}
"""


def verify_ai_response(result, subject, body):
    """
    Cross-check the AI response against the actual email to catch hallucinations.
    Returns (is_valid, reason).
    """
    if not result or not result.get("newsworthy"):
        return True, "not newsworthy — no check needed"

    title = result.get("title", "").lower()
    summary = result.get("summary", "").lower()
    evidence = result.get("evidence", "").strip()

    # Combine all email text for checking
    email_text = f"{subject}\n{body}".lower()

    # 1. Evidence field must exist and not be empty
    if not evidence or len(evidence) < 10:
        return False, "no evidence quote provided"

    # 2. Evidence must actually appear in the email (fuzzy: at least 50% of words match)
    evidence_words = set(re.findall(r'\w+', evidence.lower()))
    email_words = set(re.findall(r'\w+', email_text))
    if not evidence_words:
        return False, "evidence is empty"
    overlap = len(evidence_words & email_words) / len(evidence_words)
    if overlap < 0.4:
        return False, f"evidence quote not found in email (word overlap: {overlap:.0%})"

    # 3. Check for known hallucination patterns
    hallucination_phrases = [
        "top 100", "top 50", "top 10", "globally recognized",
        "world ranking", "clarivate", "highly cited",
        "times higher education", "qs ranking",
        "nobel", "fields medal", "turing award",
    ]
    for phrase in hallucination_phrases:
        if phrase in title or phrase in summary:
            # Only allow if the phrase also appears in the email
            if phrase not in email_text:
                return False, f"suspicious phrase '{phrase}' not found in email"

    return True, "passed"


def ask_deepseek(subject, body, sender, recipients):
    """Send email context to DeepSeek-R1 and parse the structured response."""
    # Truncate body to keep within context window
    body_excerpt = body[:2000] if body else "(empty)"

    prompt = f"""{SYSTEM_PROMPT}

--- EMAIL ---
From: {sender}
To/CC: {recipients[:500]}
Subject: {subject}
Body:
{body_excerpt}
--- END EMAIL ---

Analyze and respond with JSON only:"""

    payload = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 512,
        },
    }).encode()

    req = urllib.request.Request(
        OLLAMA_URL, data=payload,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw_response = json.loads(resp.read().decode())["response"]
    except Exception as e:
        log.warning(f"  ⚠  Ollama request failed: {e}")
        return None

    # Strip DeepSeek's <think>…</think> reasoning block
    cleaned = re.sub(r"<think>.*?</think>", "", raw_response, flags=re.DOTALL).strip()

    # Try to extract JSON
    # First try: find a JSON object
    match = re.search(r"\{[^{}]*\}", cleaned, re.DOTALL)
    if not match:
        # Second try: maybe there are nested braces (e.g. tags array)
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if not match:
        log.warning(f"  ⚠  Could not extract JSON from response")
        log.debug(f"  Raw response: {raw_response[:300]}")
        return None

    try:
        result = json.loads(match.group(0))
    except json.JSONDecodeError:
        # Try fixing common issues: single quotes, trailing commas
        fixed = match.group(0)
        fixed = fixed.replace("'", '"')
        fixed = re.sub(r",\s*}", "}", fixed)
        fixed = re.sub(r",\s*]", "]", fixed)
        try:
            result = json.loads(fixed)
        except json.JSONDecodeError:
            log.warning(f"  ⚠  JSON parse failed")
            return None

    return result


# ──────────────────────────────────────────────
# HUGO POST CREATION
# ──────────────────────────────────────────────

def create_hugo_post(result, date_str, source_email=""):
    """Write a Hugo-compatible markdown post from AI analysis."""
    title = result.get("title", "Untitled News").strip('"')
    summary = result.get("summary", "").strip('"')
    evidence = result.get("evidence", "").strip('"')
    tags = result.get("tags", [])
    category = result.get("category", "other")

    # Sanitize slug
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    slug = slug[:80]  # reasonable max length

    folder = POSTS_DIR / slug
    folder.mkdir(parents=True, exist_ok=True)

    post_path = folder / "index.md"
    if post_path.exists():
        log.info(f"  ⏭  Post already exists: {slug}")
        return slug

    # Clean tags for Hugo
    if isinstance(tags, list):
        tags_str = json.dumps(tags)
    else:
        tags_str = '["news"]'

    content = f"""---
title: "{title}"
date: {date_str}
summary: "{summary}"
tags: {tags_str}
categories: ["{category}"]
# Source email: {source_email}
# Evidence: {evidence[:200]}
---

{summary}
"""

    post_path.write_text(content, encoding="utf-8")
    log.info(f"  ✨ Created post: {slug}")
    return slug


# ──────────────────────────────────────────────
# STATE MANAGEMENT (avoid re-processing)
# ──────────────────────────────────────────────

def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            return {"processed": []}
    return {"processed": []}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


# ──────────────────────────────────────────────
# MAIN PIPELINE
# ──────────────────────────────────────────────

def should_skip_folder(folder_path):
    """Check if this folder (or any parent) is in the skip list."""
    parts = Path(folder_path).parts
    return any(p.lower().strip(".") in SKIP_FOLDERS or p.lower() in SKIP_FOLDERS for p in parts)


def is_relevant_email(msg):
    """
    Fast pre-filter (no AI). Returns True if the email is plausibly
    related to you or your professional interests.
    """
    sender = decode_mime_header(msg.get("From", "")).lower()
    subject = decode_mime_header(msg.get("Subject", "")).lower()
    recipients = get_all_recipients(msg)

    # ── Rule 1: Must involve your email in some way ──
    # Either you sent it, received it directly, or it was delivered to you
    involves_me = (
        any(tok in sender for tok in IDENTITY_TOKENS)
        or any(tok in recipients for tok in IDENTITY_TOKENS)
    )
    if not involves_me:
        return False, sender, subject, recipients

    # ── Rule 2: Keyword match in subject ──
    subject_match = any(kw in subject for kw in KEYWORDS_SUBJECT)
    if subject_match:
        return True, sender, subject, recipients

    # We'll also allow through if the email is directly addressed to one of
    # your email addresses (not just a mailing list CC). This catches
    # personal messages that might be newsworthy even without keywords.
    directly_to_me = any(addr in recipients for addr in MY_EMAILS)
    if directly_to_me:
        # Still pass it through — the AI will decide if it's newsworthy
        return True, sender, subject, recipients

    return False, sender, subject, recipients


def scan_maildir(maildir_path, after_date, dry_run=False):
    """Walk the Maildir and process relevant emails."""
    state = load_state()
    already_seen = set(state.get("processed", []))
    new_posts = []
    evaluated = 0
    skipped_seen = 0

    if after_date:
        log.info(f"🔍 Scanning {maildir_path} for emails since {after_date.date()}")
    else:
        log.info(f"🔍 Scanning {maildir_path} — ALL emails (no date limit)")
    log.info(f"   Already processed: {len(already_seen)} messages\n")

    for root, dirs, files in os.walk(maildir_path):
        if should_skip_folder(root):
            continue

        for fname in files:
            if fname.startswith("."):
                continue

            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "rb") as f:
                    msg = email.message_from_binary_file(f)

                # ── Date filter (fastest check) ──
                date_val = msg.get("Date")
                if not date_val:
                    continue
                try:
                    dt = parsedate_to_datetime(date_val)
                except Exception:
                    continue
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                if after_date and dt < after_date:
                    continue

                # ── De-duplication ──
                msg_hash = message_id_hash(msg)
                if msg_hash in already_seen:
                    skipped_seen += 1
                    continue

                # ── Relevance pre-filter ──
                relevant, sender, subject, recipients = is_relevant_email(msg)
                if not relevant:
                    continue

                # ── Body extraction ──
                body = extract_body(msg)

                # ── Optional body keyword boost ──
                # If subject didn't match keywords, check body for strong signals
                full_subject = decode_mime_header(msg.get("Subject", ""))
                body_lower = body.lower()
                subject_lower = full_subject.lower()

                has_subject_kw = any(kw in subject_lower for kw in KEYWORDS_SUBJECT)
                has_body_kw = any(kw in body_lower for kw in KEYWORDS_BODY)

                if not has_subject_kw and not has_body_kw:
                    # Neither subject nor body has strong keywords.
                    # Only proceed if it's a direct personal email (not mailing list)
                    is_mailing_list = (
                        msg.get("Precedence", "").lower() in ("bulk", "list")
                        or msg.get("List-Id") is not None
                    )
                    if is_mailing_list:
                        continue

                # ── AI Evaluation ──
                log.info(f"🧐 Evaluating: {full_subject[:100]}")
                evaluated += 1

                if dry_run:
                    log.info(f"   [DRY RUN] Would send to DeepSeek")
                    already_seen.add(msg_hash)
                    continue

                result = ask_deepseek(full_subject, body, sender, recipients)

                if result is None:
                    log.warning(f"   ⚠  AI returned no result, skipping")
                    continue

                already_seen.add(msg_hash)

                is_newsworthy = result.get("newsworthy", False)
                confidence = result.get("confidence", 0)

                if is_newsworthy and confidence >= 0.6:
                    # ── Hallucination check ──
                    valid, reason = verify_ai_response(result, full_subject, body)
                    if not valid:
                        log.warning(f"   🚫 BLOCKED — likely hallucination: {reason}")
                        log.warning(f"      AI claimed: {result.get('title', '?')}")
                        continue

                    date_str = dt.strftime("%Y-%m-%d")
                    slug = create_hugo_post(result, date_str, source_email=fpath)
                    new_posts.append({
                        "slug": slug,
                        "title": result.get("title", ""),
                        "date": date_str,
                        "category": result.get("category", ""),
                        "confidence": confidence,
                        "evidence": result.get("evidence", ""),
                        "source": fpath,
                    })
                else:
                    reason = "not newsworthy" if not is_newsworthy else f"low confidence ({confidence:.2f})"
                    log.info(f"   ⏭  Skipped: {reason}")

            except Exception as e:
                log.debug(f"   Error processing {fpath}: {e}")
                continue

    # Save state
    state["processed"] = list(already_seen)
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    save_state(state)

    return new_posts, evaluated, skipped_seen


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Scan Maildir for academic news using DeepSeek-R1 AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent("""\
            Examples:
              %(prog)s                     # scan ALL emails (no date limit)
              %(prog)s --days 90           # scan last 90 days only
              %(prog)s --dry-run           # preview what would be evaluated
              %(prog)s --reset             # clear processing state and rescan
              %(prog)s -v                  # verbose/debug output
        """),
    )
    parser.add_argument("--days", type=int, default=0,
                        help="How many days back to scan (default: 0 = all emails, no date limit)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show which emails would be AI-evaluated without calling Ollama")
    parser.add_argument("--reset", action="store_true",
                        help="Reset the processing state (re-evaluate all emails)")
    parser.add_argument("--maildir", type=str, default=None,
                        help=f"Override Maildir path (default: {MAILDIR})")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable debug logging")
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if args.reset and STATE_FILE.exists():
        STATE_FILE.unlink()
        log.info("🗑  State reset — will re-evaluate all emails")

    maildir = Path(args.maildir) if args.maildir else MAILDIR
    if not maildir.exists():
        log.error(f"❌ Maildir not found: {maildir}")
        sys.exit(1)

    after_date = None
    if args.days > 0:
        after_date = datetime.now(timezone.utc) - timedelta(days=args.days)

    new_posts, evaluated, skipped = scan_maildir(maildir, after_date, dry_run=args.dry_run)

    # Summary
    print(f"\n{'═' * 50}")
    print(f"  Scan complete!")
    print(f"  Emails AI-evaluated:    {evaluated}")
    print(f"  Already processed:      {skipped}")
    print(f"  New posts created:      {len(new_posts)}")
    print(f"{'═' * 50}")

    if new_posts:
        print("\n📰 New posts:")
        for p in new_posts:
            print(f"   [{p['date']}] {p['title']}  ({p['category']}, conf={p['confidence']:.0%})")
            print(f"            Evidence: {p.get('evidence', 'n/a')[:100]}")
            print(f"            Source:   {p.get('source', 'n/a')}")

    if args.dry_run:
        print("\n⚠  This was a DRY RUN — no AI calls were made and no posts were created.")


if __name__ == "__main__":
    main()
