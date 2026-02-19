#!/bin/bash

MAILDIR="/home/vagos/Maildir"
TARGET_EMAIL="evlachos@athenarc.gr"
# Strict list to avoid generic newsletters
KEYWORDS="submitted|manuscript|submission|peer review|decision|journal|accepted|rejected|revision|deadline|due"
MODEL="qwen2.5-coder:7b"
CURRENT_DATE="February 18, 2026"

echo "Step 1: Filtering for Athena RC emails from 2026..."

# 1. Find all files
# 2. Grep for your email address
# 3. Grep for the actual year 2026 in the Date header
# 4. Grep for your keywords
SUBJECT_LIST=$(find "$MAILDIR/new" "$MAILDIR/cur" -type f -print0 | \
    xargs -0 grep -lEi "$TARGET_EMAIL" | \
    xargs grep -l "Date: .* 2026" | \
    xargs grep -iE "$KEYWORDS" -l | \
    xargs grep -ih "^Subject: " | \
    sed 's/[Ss]ubject: //g' | \
    perl -MEncode -ne 'binmode(STDOUT, ":utf8"); print decode("MIME-Header", $_)' | \
    sort | uniq)

if [ -z "$SUBJECT_LIST" ]; then
    echo "No relevant 2026 emails found for $TARGET_EMAIL."
    exit 0
fi

echo "Step 2: Sending 2026 Activity to Ollama..."

PROMPT="Today is $CURRENT_DATE. 
Analyze these SUBJECTS from my 2026 emails:

$SUBJECT_LIST

Please provide a BRIEF summary:
1. 🟢 RECENT SUCCESS: (Accepted papers)
2. 🟡 ACTION ITEMS: (Revisions or reviews you must complete)
3. 📢 UPCOMING DEADLINES: (Only list 'Call for Papers' where the deadline is clearly AFTER $CURRENT_DATE)

Ignore any mention of years before 2026. Be extremely concise."

echo "$PROMPT" | ollama run "$MODEL"
