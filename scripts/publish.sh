#!/bin/bash

# 1. Run cleanup/maintenance scripts if needed
# python3 fix_types.py && python3 clear_trash.py

# 2. Stage only what the automation actually produces.
#    This used to be `git add -A`, which meant an unattended cron run would
#    sweep up and publish any unrelated edit left in the working tree.
#    content/publication is narrowed to the sparkline PNGs that
#    fetch_ieee_stats.py renders, so an edited paper.pdf is never swept along.
git add -A -- content/post data 'content/publication/*/sparkline.png'

# 3. Check whether anything was actually STAGED. This has to look at the index,
#    not the whole tree: with the add scoped above, an unrelated unstaged edit
#    would otherwise pass this gate and then fail `git commit` on an empty index.
if git diff --cached --quiet; then
    echo "No changes detected. Nothing to publish."
    exit 0
fi

# 4. Commit with a timestamped message
COMMIT_MSG="Site update: $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_MSG"

# 5. Push to the main branch, rebasing first so a push from another machine
#    does not leave the cron job failing silently every week.
echo "Pushing updates to GitHub..."
if ! git pull --rebase --quiet origin main; then
    echo "ERROR: rebase onto origin/main failed; resolve by hand. Nothing pushed." >&2
    exit 1
fi
git push origin main

echo "Publishing complete!"
