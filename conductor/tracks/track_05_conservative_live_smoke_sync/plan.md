# Plan - Conservative Live Smoke Sync

## Tasks
- [ ] Set `NZLC_MIN_SECONDS_BETWEEN_REQUESTS=1.0`.
- [ ] Run `uv run nzlc sync --seed-work-ids seeds/work_ids.txt --max-works 5`.
- [ ] Run `uv run nzlc validate`.
- [ ] Run `uv run nzlc manifest`.
- [ ] Run `uv run nzlc coverage-report`.
- [ ] Inspect `data/_state/sync_state.json`, `data/manifests/latest_manifest.json`, and `data/manifests/latest_changes.json`.

## Current blocker

- `NZ_LEGISLATION_API_KEY` is not configured in the local environment.
- `seeds/work_ids.txt` does not exist; only example seed files are present.
- The live sync, validation, manifest, coverage, and output inspection tasks require a successful conservative live sync first.
