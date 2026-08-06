#!/usr/bin/env node
// scripts/generate-manifest.js
//
// Scans data/1on1/ and data/idp/ for Markdown files and writes
// data/index.json, a flat manifest of relative paths (relative to data/)
// that dashboard/parser.js fetches at page load.
//
// Re-run this any time you add, remove, or rename files under data/1on1/
// or data/idp/, then reload the dashboard (or click "Refresh data").
//
// Usage: node scripts/generate-manifest.js
//
// NOTE: scripts/generate_manifest.py is a dependency-free Python mirror
// of this script (no Node required). If you change the logic here,
// update that file too so both stay byte-for-byte equivalent.

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.resolve(__dirname, '..');
const DATA_DIR = path.join(REPO_ROOT, 'data');
const SCAN_FOLDERS = ['1on1', 'idp'];

/**
 * Lists Markdown files directly under data/<folder>/, returned as
 * paths relative to data/ (e.g. "1on1/2026-01-19.md").
 * @param {string} folder
 * @returns {string[]}
 */
function listMarkdownFiles(folder) {
  const dir = path.join(DATA_DIR, folder);
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((name) => name.toLowerCase().endsWith('.md'))
    .sort()
    .map((name) => `${folder}/${name}`);
}

const files = SCAN_FOLDERS.flatMap(listMarkdownFiles);
const manifest = { files };

fs.writeFileSync(
  path.join(DATA_DIR, 'index.json'),
  JSON.stringify(manifest, null, 2) + '\n',
  'utf8'
);

console.log(`Wrote data/index.json with ${files.length} file(s).`);
