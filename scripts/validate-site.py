#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
html_path = ROOT / "docs" / "index.html"
if not html_path.exists():
    errors.append("Missing docs/index.html")
else:
    html = html_path.read_text(encoding="utf-8")
    for attr, pattern in [("script", r'<script[^>]+src="([^"]+)"'), ("stylesheet", r'<link[^>]+href="([^"]+\.css)"')]:
        for target in re.findall(pattern, html):
            if target.startswith(("http://", "https://", "//")):
                continue
            if not (ROOT / "docs" / target).exists():
                errors.append(f"Missing {attr} target: docs/{target}")
for p in ["docs/assets/app.js", "docs/assets/content.js", "docs/assets/styles.css"]:
    if not (ROOT / p).exists():
        errors.append(f"Missing required file: {p}")
if errors:
    print("SITE VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("SITE VALIDATION PASSED")
