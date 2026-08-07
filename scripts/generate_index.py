#!/usr/bin/env python3
# scripts/generate_index.py
#
# Scans data/1on1/ and data/idp/ for Markdown files and writes
# data/index.json, a flat index of relative paths (relative to data/)
# that dashboard/parser.js fetches at page load.
#
# Re-run this any time you add, remove, or rename files under data/1on1/
# or data/idp/, then reload the dashboard (or click "Refresh data").
#
# Usage: python scripts/generate_index.py

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / 'data'
SCAN_FOLDERS = ['1on1', 'idp']


def list_markdown_files(folder):
    """Lists Markdown files directly under data/<folder>/, returned as
    paths relative to data/ (e.g. "1on1/2026-01-19.md")."""
    directory = DATA_DIR / folder
    if not directory.exists():
        return []
    names = sorted(
        entry.name for entry in directory.iterdir()
        if entry.name.lower().endswith('.md')
    )
    return [f'{folder}/{name}' for name in names]


files = [f for folder in SCAN_FOLDERS for f in list_markdown_files(folder)]
index_data = {'files': files}

with open(DATA_DIR / 'index.json', 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(index_data, indent=2) + '\n')

print(f'Wrote data/index.json with {len(files)} file(s).')
