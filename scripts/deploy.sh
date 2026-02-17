#!/bin/bash

# --- CONFIGURATION ---
SITE_ROOT="$HOME/www/evlachos_website"
REMOTE_USER="vagos"              # Change to your server username
REMOTE_HOST="evlachos.space"     # Your server address
REMOTE_DIR="/var/www/evlachos/"  # Path on the server
# ---------------------

cd "$SITE_ROOT" || exit

# 1. Clean previous build artifacts
echo "🧹 Cleaning up..."
rm -rf public/ resources/
hugo mod clean

# 2. Start Hugo dev server
echo "🚀 Starting Hugo dev server at http://localhost:1313"
hugo server \
  --gc \
  --cleanDestinationDir \
  --disableFastRender \
  --bind 127.0.0.1
