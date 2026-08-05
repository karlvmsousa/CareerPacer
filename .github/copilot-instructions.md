# CareerPacer — Project Context for AI Assistance

## What this is
CareerPacer is an open-source, AI-assisted system for tracking career growth:
1:1 meeting discussions, performance reviews, and an Individual Development
Plan (IDP). It solves the problem of career-development signal (feedback,
action plans, growth areas) getting lost across scattered notes instead of
being acted on.

## Architecture principles (do not violate these without discussion)
- No backend, no database. All data is plain Markdown files with YAML
  frontmatter, stored under `data/`. Git-friendly and portable by design.
- The "intelligence" layer is an Agent Skill (`SKILL.md`, following the open
  Agent Skills format), which parses freeform notes into structured entries.
  Do not assume a different LLM framework unless asked.
- The dashboard (`dashboard/`) is static HTML/JS only — no build step,
  no backend.
- Any feature requiring external credentials/API access (e.g. calendar
  sync) is explicitly out of core scope — see `docs/future-ideas.md`.
- `data/` is gitignored — real personal career data is never committed.
  `examples/data/` holds the committed John/PulseFit sample persona used
  for demos.

## Core entities (the ontology)
- `OneOnOne` — a single 1:1 meeting record (date, attendees, discussion,
  follow-ups, linked IDP actions). Status lifecycle: `draft` (prep note,
  meeting hasn't happened) → `logged` (real notes, meeting happened)
- `PerformanceEval` — a formal review record (period, type, strengths,
  growth areas)
- `IDPAction` — an Individual Development Plan action item (title, status,
  start/target date, linked evidence). Status lifecycle:
  not_started → in_progress → {done | blocked}

Full definitions: `docs/terminology.md`. Business rules and relationships
(still being formalized): `docs/ontology.md`. Structure comes from
`schema/*.json`; voice/tone/format for entry prose comes from
`docs/style-guide.md` — the two are complementary sources of truth.

## Current status: MVP-first
We are building toward a minimal viable version before adding anything else.
See `backlog.md` for the actual current priority order — always check it
before assuming what to build next. Do not implement Post-MVP items
(Performance Eval schema, Intake onboarding, .ics generation, i18n, etc.)
unless explicitly asked; they are intentionally deferred.

## Conventions
- Markdown files use YAML frontmatter for structured fields, plain prose
  for freeform content.
- Keep schema definitions and any validation logic consistent with
  `docs/terminology.md` — it's the source of truth for naming.
- Prefer full words over abbreviations in field/folder/file names, with
  documented exceptions for established domain acronyms (`IDP`, `OKR`,
  `PIP`, `1:1`) — see `docs/terminology.md`'s "Naming conventions"
  section.
- The dashboard must be served via a local static server (`npx serve`, or
  `python -m http.server` bound to `127.0.0.1`) — opening `index.html`
  directly via `file://` won't work, since data loads via `fetch()`.
- This started as a personal open-source project and is aimed at being
  broadly useful, with community contributions welcome. Keep license
  (MIT) and attribution clean.

## When context is missing
If something isn't covered in `backlog.md`, `docs/terminology.md`, or
`docs/future-ideas.md`, ask rather than assuming — this project has a
deliberately scoped architecture and I'd rather clarify than have you
guess wrong.