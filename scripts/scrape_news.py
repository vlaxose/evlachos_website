#!/usr/bin/env python3
import argparse
import email
import json
import os
import re
import urllib.request
from datetime import datetime, timedelta, timezone
from email.header import decode_header
from email.utils import parsedate_to_datetime
from pathlib import Path
from textwrap import dedent

# --- CONFIGURATION ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1:8b" 
MAILDIR = Path.home() / "Maildir"
SITE_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = SITE_ROOT / "content" / "post"

# Strict filter: Only process emails sent from this address
TARGET_SENDER = "evlachos@athenarc.gr"

def decode_mime(header):
    """Decodes MIME headers, handling specific Greek and unknown-8bit encodings."""
    if not header: return ""
    try:
        parts = decode_header(header)
        decoded_parts = []
        for data, encoding in parts:
            if isinstance(data, bytes):
                enc = encoding if encoding and encoding != 'unknown-8bit' else "utf-8"
                try:
                    decoded_parts.append(data.decode(enc))
                except:
                    # Fallback for standard Greek encoding common in academic mail
                    decoded_parts.append(data.decode("iso-8859-7", errors="replace"))
            else:
                decoded_parts.append(str(data))
        return "".join(decoded_parts)
    except Exception:
        return str(header)

def extract_json(text):
    """Strips DeepSeek-R1 <think> tags to extract the JSON payload."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None

def get_email_body(msg):
    """Extracts plain text body for AI analysis."""
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    body += payload.decode(errors="replace")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(errors="replace")
    return body[:1500]

def ask_deepseek(subject, body):
    """Uses DeepSeek-R1 to classify academic milestones."""
    prompt = f"""
    Analyze this email for Dr. Evangelos Vlachos (ATHENA RC).
    Is this a professional milestone? (Paper, Award, Funding, ΔΣ Meeting, or Internship).
    
    Subject: {subject}
    Body excerpt: {body}
    
    Respond ONLY in JSON: {{"newsworthy": true, "title": "Title", "summary": "Summary", "tags": ["tag1"]}}
    """
    payload = json.dumps({"model": MODEL, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            raw_response = json.loads(resp.read().decode())['response']
            return json.loads(extract_json(raw_response))
    except Exception: return None

def create_hugo_post(data, dt):
    """Creates a markdown post in the Hugo content directory."""
    slug = re.sub(r'\W+', '-', data['title'].lower()).strip('-')
    folder_path = POSTS_DIR / slug
    folder_path.mkdir(parents=True, exist_ok=True)
    
    content = dedent(f"""\
        ---
        title: "{data['title']}"
        date: {dt.strftime('%Y-%m-%d')}
        summary: "{data['summary']}"
        tags: {data['tags']}
        ---
        {data['summary']}
    """)
    (folder_path / "index.md").write_text(content)
    print(f"  ✨ Hugo Post Created: {slug}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=65) # Covers early January
    args = parser.parse_args()

    after_date = datetime.now(timezone.utc) - timedelta(days=args.days)
    print(f"🔍 Deep Scanning ALL Maildir folders for mail from {TARGET_SENDER}...")

    found_any = False
    # Walk through ALL folders, including hidden ones like .Sent
    for root, dirs, files in os.walk(MAILDIR):
        for fname in files:
            # Skip hidden files that aren't emails
            if fname.startswith('.'): continue
            
            file_path = os.path.join(root, fname)
            try:
                with open(file_path, "rb") as f:
                    msg = email.message_from_binary_file(f)
                    
                    # Check 'From' and 'Return-Path' to ensure we capture sent mail
                    sender = decode_mime(msg.get("From", "")).lower()
                    ret_path = decode_mime(msg.get("Return-Path", "")).lower()

                    if TARGET_SENDER not in sender and TARGET_SENDER not in ret_path:
                        continue

                    date_val = msg.get("Date")
                    if not date_val: continue
                    dt = parsedate_to_datetime(date_val)
                    if dt.tzinfo is None: dt = dt.replace(tzinfo=timezone.utc)
                    if dt < after_date: continue

                    found_any = True
                    subject = decode_mime(msg["Subject"])
                    print(f"🧐 Found Sent Email: {subject} ({dt.date()})")
                    
                    result = ask_deepseek(subject, get_email_body(msg))
                    if result and result.get("newsworthy"):
                        create_hugo_post(result, dt)
            except Exception: continue

    if not found_any:
        print("❌ Still no emails found. Please verify the folder name of your 'Sent' mail.")

if __name__ == "__main__":
    main()
