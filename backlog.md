# Backlog

Simple three-column backlog for tracking project progress. Move items between
sections as work advances. Keep entries short; link to issues/PRs once the
repo has them.

---

## 📋 Todo

### 🎯 MVP — first launch
- [x] Scaffold repo structure (folders: `data/`, `schema/`, `dashboard/`, `docs/`)
- [x] Write minimal schema for `OneOnOne` and `IDPAction` only (informal JSON Schema, just enough to structure the Skill's output and parse in the dashboard — formal validation/linting comes later)
- [x] Write `SKILL.md` v1 — handles two things only: (1) turn freeform 1:1 notes into a structured `data/1on1s/*.md` file, (2) create/update `IDPAction` entries and link them to 1:1s
- [x] Build `dashboard/parser.js` (fetch + parse frontmatter from `data/`)
- [x] Build `dashboard/index.html` — 1:1 timeline view
- [x] Build `dashboard/index.html` — IDP kanban board (not started/in progress/done/blocked)
- [x] Add sample/seed data so the dashboard is demoable out of the box
- [x] Add LICENSE (MIT) — do this **before** any company involvement
- [ ] Trim README to reflect actual MVP scope (remove/flag features not yet built)

### 🚀 Post-MVP (fast follow)
- [ ] Write JSON Schema for `PerformanceEval` entity
- [ ] `dashboard/index.html` — performance eval history view
- [ ] Design "Intake" — first-run onboarding flow (1:1 cadence, whether to track Evals/IDP, manager's name)
- [ ] Add `.ics` generation to the Skill (on-demand, no persistence)
- [ ] Formal JSON Schema validation script + referential-integrity check (linked_actions must exist in idp/actions.md) — good scope for the data-engineer collaborator
- [ ] Write CONTRIBUTING.md
- [ ] Dashboard i18n (English/Portuguese string tables, see docs/future-ideas.md)

## 🔄 Ongoing

- [ ] `docs/terminology.md` — glossary of career/performance-review terms + ontology terms (living document, will grow as we refine the model)
- [ ] `docs/ontology.md` — entity/relationship/business-rule documentation

## ✅ Done

- [x] Defined initial pain point and solution concept
- [x] Chose architecture: Markdown + YAML frontmatter, Claude Skill, static HTML dashboard
- [x] Drafted initial data model (OneOnOne, PerformanceEval, IDPAction, NextMeetingDraft)
- [x] Decided v1 scope: full stack (1:1s + Evals + IDP + dashboard), later re-scoped into MVP + Post-MVP phases
- [x] Chose project name: CareerPacer (backronym: Progress-Aware Conversational Evaluation Routine)
