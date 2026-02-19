#!/bin/bash

# 1. Run cleanup/maintenance scripts if needed
# python3 fix_types.py && python3 clear_trash.py

# 2. Stage all changes
# -A (or --all) adds new files, modifies tracked files, and removes deleted files
git add -A

# 3. Check if there are actually changes to commit
if git diff-index --quiet HEAD --; then
    echo "No changes detected. Nothing to publish."
    exit 0
fi

# 4. Commit with a timestamped message
COMMIT_MSG="Site update: $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_MSG"

# 5. Push to the main branch
echo "Pushing updates to GitHub..."
git push origin main

echo "Publishing complete!"
