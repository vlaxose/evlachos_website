#!/usr/bin/env python3
import argparse
import email
import json
import os
import urllib.request
from datetime import datetime, timedelta, timezone
from email.header import decode_header
from email.utils import parsedate_to_datetime
from pathlib import Path

# --- CONFIGURATION ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1:8b"  # Specifically using DeepSeek-R1 8b as requested
MAILDIR = Path.home() / "Maildir"
SITE_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = SITE_ROOT / "content" / "post"

# Trusted senders bypass the keyword filter
TRUSTED_SENDERS = ["kokkali@athenarc.gr", "stylios@athenarc.gr"]

def decode_mime(header):
    if not header: return ""
    parts = decode_header(header)
    return "".join([
        (p[0].decode(p[1] or "utf-8", errors="replace") if isinstance(p[0], bytes) else p[0])
        for p in parts
    ])

def get_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode(errors="replace")
    return msg.get_payload(decode=True).decode(errors="replace") if msg.get_payload() else ""

def ask_deepseek(subject, body):
    """Uses DeepSeek-R1 to determine if an email is a personal academic milestone."""
    prompt = f"""
    You are an AI assistant for Dr. Evangelos Vlachos (ISI/Athena RC). 
    Research areas: ISAC, 6G, UAV swarms, Signal Processing.

    Analyze this email. Is it a significant personal milestone (Paper accepted, 
    Award won, New Grant/Funding, Keynote invitation, or Official Appointment)? 
    
    Email Subject: {subject}
    Email Body: {body[:1000]}

    Respond ONLY in JSON format:
    {{
      "newsworthy": true/false,
      "title": "Concise English Title",
      "summary": "1-sentence summary",
      "tags": ["6g", "award", "etc"]
    }}
    """
    
    data = json.dumps({"model": MODEL, "prompt": prompt, "stream": False, "format": "json"}).encode()
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
    
    try:
        with urllib.request.urlopen(req) as resp:
            response = json.loads(resp.read().decode())
            return json.loads(response['response'])
    except:
        return {"newsworthy": False}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=60) # To catch that Jan 12th email
    args = parser.parse_args()

    after_date = datetime.now(timezone.utc) - timedelta(days=args.days)
    
    for subdir in ["new", "cur"]:
        for fname in os.listdir(MAILDIR / subdir):
            with open(MAILDIR / subdir / fname, "rb") as f:
                msg = email.message_from_binary_file(f)
                dt = parsedate_to_datetime(msg["Date"])
                if dt.tzinfo is None: dt = dt.replace(tzinfo=timezone.utc)
                
                if dt < after_date: continue
                
                sender = decode_mime(msg["From"]).lower()
                subject = decode_mime(msg["Subject"])
                
                # Check for Athena Kokkali's email specifically
                if any(ts in sender for ts in TRUSTED_SENDERS) or "πρακτική" in subject.lower():
                    print(f"🤖 DeepSeek Analyzing: {subject}")
                    result = ask_deepseek(subject, get_body(msg))
                    
                    if result.get("newsworthy"):
                        print(f"✅ SUCCESS: {result['title']}")
                        # Hugo post creation logic goes here...

if __name__ == "__main__":
    main()
