#!/bin/bash
# Start Hugo development server with live reload

SITE_ROOT="$HOME/www/evlachos_website"
cd "$SITE_ROOT" || exit

rm -rf resources/ public/
hugo mod clean

echo "Starting Hugo dev server at http://localhost:1313"
hugo server \
  --gc \
  --cleanDestinationDir \
  --disableFastRender \
  --bind 127.0.0.1
