# Backlog

Simple backlog for tracking project progress, grouped by theme.
Move items between Done/Planned as work advances.
Keep entries short; link to issues/PRs once the repo has them.

---

## 🧩 Core data model & schema

### Done
- Minimal JSON Schema for `OneOnOne` and `IDPAction`
- JSON Schema for `PerformanceEval`
- Drafted initial data model (`OneOnOne`, `PerformanceEval`, `IDPAction`, `NextMeetingDraft`)

### Planned
- (none currently — data model is stable pending the Post-MVP feature work tracked below)

## 🤖 Skill / agent behavior

### Done
- SKILL.md v1: freeform 1:1 notes → structured `data/1on1/*.md`; create/update `IDPAction` entries linked to 1:1s, with Boundaries clarifying body prose stays informal while frontmatter is hard-validated
- Step 6 self-validation: Skill runs `validate_data.py` on its own output before considering a task done

### Planned
- Design "Intake" — first-run onboarding flow (1:1 cadence, whether to track Evals/IDP, manager's name)
- Add `.ics` generation to the Skill (on-demand, no persistence)

## 📊 Dashboard

### Done
- `dashboard/parser.js` (fetch + parse frontmatter from `data/`)
- 1:1 timeline view
- IDP kanban board (not started/in progress/done/blocked)
- Sample/seed data so the dashboard is demoable out of the box
- Rebuilt data loading: local-server + fetch model (dropped folder-picker), `generate_index.py` → `data/index.json`
- Redesigned Overview tab: profile personalization, unified layout width, "Next 1:1 Prep"/"Recent Progress"
- Pinned `js-yaml` CDN script to an exact version with an SRI hash (supply-chain hardening)

### Planned
- Performance eval history view
- i18n (English/Portuguese string tables, see `docs/future-ideas.md`)

## 🛠️ Tooling & CI

### Done
- Repo scaffolding (`data/`, `schema/`, `dashboard/`, `docs/`)
- `.gitignore`; real personal data stays private, `examples/data/` holds the committed demo persona
- Formal JSON Schema validation script + referential-integrity check (`scripts/validate_data.py`, `requirements.txt`)
- GitHub Actions CI: runs the validation script against schema/examples on every push and PR

### Planned
- (none currently)

## 📚 Docs & contribution

### Done
- LICENSE (MIT)
- Trimmed README to actual MVP scope
- `docs/style-guide.md` (voice/tone/format conventions)
- Converted example data to first-person voice per style-guide
- CONTRIBUTING.md
- Fixed stale README/SKILL.md claims (Prerequisites pip-install gap, Step 6 vs. Boundaries contradiction), reformatted prose to one-sentence-per-line

### Planned / Ongoing
- `docs/terminology.md` — glossary of domain + ontology terms (living document, grows as the model is refined)
