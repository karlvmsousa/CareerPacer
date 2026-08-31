---
name: careerpacer-1on1-and-idp
description: >-
  Turn freeform 1:1 meeting notes into a structured CareerPacer OneOnOne
  file under data/1on1/, and create or update IDPAction entries in the
  current year's data/idp/<year>.md, linked back to that 1:1. Use this
  skill when the user dictates or pastes notes from a 1:1 that just
  happened or is upcoming, or asks to "log a 1:1", "write up this
  meeting", "prep for my next 1:1", "add/update an IDP action", or "link
  this to my growth plan".
---

# CareerPacer: 1:1 + IDP Skill (v1)

## Scope (v1)

This skill handles exactly two things:

1. Turning freeform 1:1 notes into a structured `data/1on1/*.md` file
   that matches `schema/1on1.schema.json`. This includes both logging a
   1:1 that just happened (`status: logged`) and drafting a prep note
   for an upcoming one (`status: draft`) — see Step 2.
2. Creating or updating `IDPAction` entries in the current year's
   `data/idp/<year>.md` file (per `schema/idp-action.schema.json`) and
   linking them to the 1:1 that raised or advanced them.

Everything else in CareerPacer — performance evaluations
(`data/evaluation/`), the dashboard — is out of scope for v1. Don't
create or edit those.

This skill has two sources of truth: the two JSON schemas define
*structure* (fields, types), and `docs/style-guide.md` defines *how the
prose within those fields should read* (voice, tone, format). The body
prose is freeform and informal, not schema-validated — but the
frontmatter itself is self-checked against the schemas before the task
is considered done (see Step 6). `examples/data/1on1/2026-06-15.md` +
`examples/data/idp/2026.md` are an optional illustrative reference for
shape/format only — `schema/*.json` and `docs/style-guide.md` remain
the sole sources of truth; don't infer structure or voice from the
examples alone.

## Step 1: Read the input

You'll usually be given freeform text — dictated or pasted notes from a
1:1 that already happened (`status: logged`). You may instead be asked to
prep talking points for a 1:1 that hasn't happened yet (`status: draft`)
— in that case, work from whatever context is available (recent 1:1s,
open IDP actions) instead of live notes. For a `logged` 1:1, identify:
- The date of the meeting (ask if not stated or inferable)
- Who was there (attendees)
- What was discussed
- Any quick, short-term follow-ups
- Any items that sound like durable development goals (candidates for an
  `IDPAction` — see Step 3)

## Step 2: Write the OneOnOne file

- Path: `data/1on1/<date>.md`, where `<date>` is `YYYY-MM-DD` (the actual
  or planned meeting date).
- Frontmatter (see `schema/1on1.schema.json`):
  - `id`: `1on1-<YYYY-MM-DD>` (matches the filename)
  - `date`: `YYYY-MM-DD`
  - `status`: `logged` if the meeting already happened and these are real
    notes; `draft` if you're prepping talking points for a meeting that
    hasn't happened yet
  - `attendees`: array of names
  - `follow_ups`: short freeform action items that do **not** need
    dates/status tracking (see Step 3 for what does)
  - `linked_actions`: IDs of any `IDPAction`s created or touched in Step
    3–4 (fill this in after those steps)
  - `tags`: optional, freeform
- Body: plain Markdown prose capturing the discussion, following
  `docs/style-guide.md` — first person, bullet points, one idea per
  bullet. This is freeform and not schema-validated.
- **Drafting a prep note for an upcoming 1:1** is not a separate file or
  folder — create (or update) the same `data/1on1/<date>.md` file with
  `status: draft` and prep bullets in the body. Once the meeting actually
  happens, update that same file in place with the real discussion and
  flip `status` to `logged` — don't create a second file.

## Step 3: Decide what's IDP-worthy

Not every follow-up deserves a persistent `IDPAction`. Use this rule of
thumb:

- Keep it as a `OneOnOne.follow_ups` entry if it's a one-off task or too
  vague to track with a start/target date (e.g. "share the deployment
  runbook").
- Promote it to an `IDPAction` if it's a recurring theme or a concrete
  development goal that's worth tracking over time with a status and
  dated evidence (e.g. "ship and monitor a production model",
  "build visibility in leadership meetings").

If it's ambiguous, prefer **not** creating a new `IDPAction` — ask the
user, or leave it as a `follow_up` and revisit at the next 1:1. Don't
invent a target date, status, or evidence the notes didn't actually
support.

## Step 4: Create or update IDPAction entries

File: `data/idp/<current_year>.md` (the year the action is first
created, not necessarily the year it's due — see file header comment in
`schema/idp-action.schema.json`). If it doesn't exist yet, create it with:

```yaml
---
year: <current_year>
actions: []
---
```

For each IDP-worthy item from Step 3:

- **First check if it matches an existing action** (similar `title` /
  topic, not necessarily exact wording). If it does, don't create a
  duplicate — instead:
  - Append a new date-prefixed entry to that action's `linked_evidence`,
    e.g. `"[2026-07-13] <what happened>"`.
  - Update `status` if the notes support it (e.g. `not_started` →
    `in_progress` once real work has started; → `done` or `blocked` if
    the notes say so explicitly). Don't advance status on inference alone.
- **Otherwise, create a new action** appended to the `actions` array:
  - `id`: `idp-<year>-<NNN>`, zero-padded, next unused number in that
    year's file (e.g. `idp-2026-004`)
  - `title`: short description of the development goal
  - `status`: `not_started` unless the notes clearly show work already
    in progress
  - `start_date`: usually the date of this 1:1
  - `target_date`: only set if the user gave one or a clear timeframe —
    otherwise omit rather than guessing
  - `source`: the 1:1's `id` (e.g. `1on1-2026-07-13`)
  - `linked_evidence`: optional at creation; add an initial entry if the
    notes already describe concrete progress

Only create or update `IDPAction` entries from a `logged` 1:1 — don't
promote items out of a `draft` prep note until the meeting has actually
happened and the file is flipped to `logged`.

## Step 5: Link them together

- Add every `IDPAction` id touched in Step 4 to that 1:1's
  `linked_actions` array (back in Step 2's file).
- Don't duplicate the full discussion between the two files: the
  `OneOnOne` body holds the complete narrative; `IDPAction.linked_evidence`
  entries should be terse, one-line, date-prefixed progress notes, not a
  copy-paste of the 1:1 body.

## Step 6: Validate before finishing

After writing or updating a `data/1on1/*.md` or `data/idp/<year>.md` file
(Steps 2–5), self-check your own output by running:

```
python scripts/validate_data.py <path/to/file.md>
```

Run it once per file you touched in this turn. If it reports a `FAIL`
(schema error or referential-integrity error, e.g. a `linked_actions` id
that doesn't exist), fix the file and re-run the script — don't consider
the task done until every file you touched passes. If the script itself
errors out because `jsonschema`/`pyyaml` aren't installed, tell the user
to run `pip install -r requirements.txt` rather than skipping the check.

## Conventions (from the schemas — keep output consistent with these)

- IDs: `1on1-<YYYY-MM-DD>` and `idp-<YYYY>-<NNN>`.
- Dates: always `YYYY-MM-DD`.
- 1:1 status lifecycle: `draft` (prep note, meeting hasn't happened) →
  `logged` (real notes, meeting happened).
- IDPAction status lifecycle: `not_started` → `in_progress` → (`done` |
  `blocked`).
- `linked_evidence` is free text, not strict IDs, but always date-prefixed:
  `"[YYYY-MM-DD] <free text>"`.

## Boundaries (don't do this in v1)

- Don't create or edit `data/evaluation/` (performance evaluations) —
  deferred, out of scope.
- Don't hard-validate against the JSON Schemas or reject input that
  doesn't perfectly fit — this is intentionally informal for MVP. Treat
  the schemas as a structural guide.
- Don't silently invent dates, statuses, or evidence the notes don't
  support — ask the user instead.
