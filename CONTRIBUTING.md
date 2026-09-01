# Contributing

CareerPacer is early-stage and mostly a one-to-two-person effort right now, so this is short on purpose.

- Opening a PR? Fill out `.github/PULL_REQUEST_TEMPLATE.md` (Goal, Changes, Testing/Validation, Notes for reviewer) — that's the process, no extra forms needed.
- Branch naming: `feature/<short-description>` (e.g. `feature/data-validation-script`).
- Touching `schema/*.json` or anything under `data/`? Run the validator before you push:
  ```
  pip install -r requirements.txt
  python scripts/validate_data.py
  ```
  CI runs this too on push/PR, but catching it locally first saves a round trip.
- The project is local-first on purpose: no backend, no database, no cloud dependency. If you're thinking about something that assumes one (a different stack, a hosted service, etc.), open an issue first so we can talk through whether/how it fits before you sink time into a PR.

MIT licensed, not v1.0 yet — things can still move around.
