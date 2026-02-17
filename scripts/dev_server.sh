#!/bin/bash

# 1. Define paths
SITE_ROOT="$HOME/www/evlachos_website"
VENV_PATH="$HOME/www/evlachos_venv"

# 2. Navigate to site
cd "$SITE_ROOT" || exit

# 3. Activate the clean virtual environment (silently)
source "$VENV_PATH/bin/activate"

# 4. Clean previous build artifacts (The "Gentoo" Scrub)
echo "🧹 Cleaning cache and resources..."
rm -rf resources/ public/
hugo mod clean

# 5. Start the Server with "Fritz!Box" settings
echo "🚀 Starting Dr. Vlachos Research Site..."
echo "   - Mode: Light (Forced)"
echo "   - Font: Source Sans 3"
echo "   - URL:  http://localhost:1313"

# Force regeneration to ensure CSS overrides apply
hugo server \
  --gc \
  --cleanDestinationDir \
  --disableFastRender \
  --config hugo.yaml
