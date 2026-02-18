#!/bin/bash
# Καθαρισμός trash (προαιρετικά)
# python fix_types.py && python clear_trash.py

# Push στο GitHub
git add .
git commit -m "Site update: $(date)"
git push origin main
