# Terminology

> **Status:** 🔄 Ongoing — this is a living glossary. Add terms as they come up
> during development or as new career-process vocabulary gets folded in.

This file defines two kinds of terms: **domain terms** (career/HR process
vocabulary this project models) and **ontology terms** (technical vocabulary
used to describe the project's own architecture). Keeping both in one place
avoids ambiguity when domain and technical meanings could collide (e.g.
"Action").

---

## Domain terms (career & performance process)

| Term | Definition |
|---|---|
| **1:1 (One-on-One)** | Recurring, informal sync between an employee and their manager. Not a formal HR process — cadence and structure vary by team. |
| **Performance Review / Performance Appraisal** | Formal, scheduled evaluation of an employee's performance, typically annual or semi-annual. |
| **Annual Performance Review (APR)** | A performance review conducted once per year. |
| **Mid-year Review / Year-end Review** | The two checkpoints in companies that run performance cycles twice a year. |
| **360-Degree Feedback** | A performance review that incorporates input from peers and/or direct reports, not just the manager. |
| **Calibration** | A process (common at larger companies) where multiple managers align ratings across a team or org to ensure consistency. |
| **IDP (Individual Development Plan)** | A plan, usually agreed upon with a manager, listing concrete development goals with target dates. Also called Growth Plan, Career Development Plan (CDP), or PDP (Personal Development Plan). |
| **PIP (Performance Improvement Plan)** | A remedial plan (not developmental) issued when performance falls below expectations. Structurally similar to an IDP (goals + dates + check-ins) but different intent — included here so the schema can accommodate it if ever needed. |
| **OKR (Objectives and Key Results)** | A goal-setting framework some companies use instead of, or alongside, an IDP. Objective = qualitative goal; Key Results = measurable outcomes. |
| **Growth Area** | A skill or behavior identified (usually in a Performance Review) as needing development. Often the seed for a new IDP Action. |
| **Evidence** | A concrete, dated artifact or event that demonstrates progress toward an IDP Action (e.g. "led the Q3 migration project," with a link or reference). |

---

## Ontology / architecture terms (how we describe the project itself)

| Term | Definition |
|---|---|
| **Ontology** | The conceptual model of this project's domain: what entities exist, how they relate, and what rules govern them — independent of file format or code. |
| **Entity** | A distinct concept in the domain that has its own identity and lifecycle (e.g. `OneOnOne`, `IDPAction`). Not the same as a database table — in this project, an entity is represented as a Markdown file with YAML frontmatter. |
| **Schema** | The technical, machine-checkable definition of an entity's structure (fields, types, required/optional), expressed as JSON Schema. The single source of truth used by both the Skill and the dashboard parser. |
| **Relationship** | A directional or bidirectional link between two entities (e.g. a `OneOnOne` *references* an `IDPAction`). |
| **Business Rule** | A constraint or behavior that must hold true regardless of implementation (e.g. "an IDPAction's start_date must be before its target_date"). |
| **Frontmatter** | The YAML block at the top of a Markdown file, delimited by `---`, holding an entity's structured fields. |
| **Skill** | The Agent Skill that encodes parsing logic, business rules, and generation behavior (e.g. turning freeform dictation into a structured `OneOnOne` file). |
| **Referential Integrity** | The guarantee that an ID referenced in one file (e.g. `linked_actions: [idp-003]`) actually exists in the target file. Enforced by the Skill on write, and optionally validated by the dashboard on read. |

---

## Open questions to resolve as terminology firms up

- Should `PerformanceEval` support a numeric `rating` field, given not all
  companies use one, and some explicitly discourage recording it outside
  official HR systems?
