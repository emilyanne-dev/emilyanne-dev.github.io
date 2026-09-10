#!/bin/bash
# Re-renders assets/files/emily-sarale-alberti-resume.pdf from resume.html.
#
# Run this after any resume edit, otherwise the Download PDF button on the
# About page will still serve the previous version:
#     python3 generate.py && ./make_resume_pdf.sh
#
# Prints from a file:// URL rather than the preview server — the preview
# server isn't reachable from a plain shell. Google Fonts still loads over
# the network, so the PDF keeps Fraunces and Space Mono.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="$ROOT/assets/files/emily-sarale-alberti-resume.pdf"

mkdir -p "$ROOT/assets/files"

"$CHROME" \
  --headless \
  --disable-gpu \
  --no-pdf-header-footer \
  --virtual-time-budget=12000 \
  --print-to-pdf="$OUT" \
  "file://$ROOT/resume.html" 2>/dev/null

echo "Wrote $OUT ($(du -h "$OUT" | cut -f1))"
