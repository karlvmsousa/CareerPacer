# CareerPacer

> ⚠️ **Status: MVP functional, pre-launch.** Core architecture, schema,
> and dashboard are in place — see [`backlog.md`](./backlog.md) for
> remaining items before the first public release.

**CareerPacer** is an open-source, AI-assisted system for tracking your
career: 1:1 meeting discussions, performance reviews, and your Individual
Development Plan (IDP) — all in one place, all in plain text, all versioned
in git.

<sub>Yes, it's also a backronym: **P**rogress-**A**ware **C**onversational
**E**valuation **R**outine.</sub>

## The problem

1:1 conversations and performance feedback contain real signal about your
strengths, growth areas, and agreed-upon action plans — but that signal
usually gets lost across scattered notebooks, docs, and memory. The result:
you *know* what you should be working on, but rarely translate it into daily
action, and you struggle to show others concrete evidence of your growth.

## The approach

- **Plain Markdown storage.** Every 1:1, performance review, and IDP action
  is a Markdown file with YAML frontmatter — human-readable, diffable in git,
  and portable (no database, no lock-in).
- **An Agent Skill as the intelligent layer.** Built on the open Agent
  Skills format, the Skill turns freeform notes ("just talked to my manager
  about...") into structured entries, links them to existing IDP goals,
  drafts prep notes for your next 1:1, and flags overdue or unsupported IDP
  actions.
- **A static HTML dashboard for review.** No backend required — the
  dashboard reads the Markdown data directly and renders a 1:1 timeline, an
  IDP progress board, and performance-review history.

## Architecture at a glance

```
careerpacer/
├── data/               # Your actual career data (Markdown + YAML frontmatter)
│   ├── 1on1/
│   ├── evaluation/
│   ├── idp/
│   ├── profile.json    # Your name/role/company/manager (lightweight, static)
│   └── index.json      # Generated manifest the dashboard fetches (see scripts/)
├── examples/
│   └── data/           # Sample John/PulseFit persona (copy into data/ for a demo)
├── schema/             # JSON Schema definitions — single source of truth
├── scripts/            # generate-manifest.js — regenerates data/index.json
├── SKILL.md            # The Agent Skill definition
├── dashboard/          # Static HTML/JS dashboard
└── docs/
    ├── terminology.md  # Glossary of domain + ontology terms
    └── style-guide.md  # Voice/tone/format conventions for entry prose
```

The core entities are `OneOnOne`, `PerformanceEval`, and `IDPAction`. See
`schema/*.json` for structure, [`SKILL.md`](./SKILL.md) for the
relationships and business rules that link them, and
[`docs/terminology.md`](./docs/terminology.md) for definitions of the
vocabulary used throughout this project.

## How to use it

1. Clone the repo. `data/` starts empty — it's gitignored, so your real
   career data never gets committed.
2. **To see the dashboard with demo content:** copy the contents of
   `examples/data/` into `data/`:
   - macOS/Linux: `cp -r examples/data/* data/`
   - Windows (PowerShell): `Get-ChildItem -Path examples\data | Copy-Item -Destination data -Recurse -Force`

   **For real use:** skip that and just start creating
   files directly under `data/` — talk to the Skill (via an AI assistant
   that supports Agent Skills) to log a 1:1 or prep for one, and it
   files structured entries under `data/1on1/` and `data/idp/`. Either
   way, `data/` stays private and untracked.
3. After adding or editing any files under `data/1on1/` or `data/idp/`,
   regenerate `data/index.json` (the manifest the dashboard fetches):
   - Node: `node scripts/generate-manifest.js`
   - Python (no Node required): `python scripts/generate_manifest.py`
4. From the repo root, start a local static server — e.g. `npx serve`,
   or `python -m http.server 8000 --bind 127.0.0.1` as a no-Node
   fallback — and open the dashboard through the URL it prints. Don't
   open `dashboard/index.html` directly by double-clicking it: dashboard
   data loads via `fetch()`, which requires http(s) and won't work over
   a `file://` URL. Click "Refresh data" in the dashboard header any
   time you regenerate the manifest or edit data without reloading the
   page.

## Documentation

- [`docs/terminology.md`](./docs/terminology.md) — glossary of domain + ontology terms
- [`docs/style-guide.md`](./docs/style-guide.md) — voice/tone/format conventions for entry prose
- [`docs/future-ideas.md`](./docs/future-ideas.md) — proposed enhancements out of core scope

## Contributing

Contribution guidelines will be added once the core schema stabilizes — see
`backlog.md` for current priorities, and
[`docs/future-ideas.md`](./docs/future-ideas.md) for proposed enhancements
(like calendar integration) that are open for discussion and community
implementation. Issues and forks are welcome in the meantime.

## License

MIT — see [LICENSE](./LICENSE).
