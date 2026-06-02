# Plan - Conservative Live Smoke Sync

## Tasks
- [ ] Set `NZLC_MIN_SECONDS_BETWEEN_REQUESTS=1.0`.
- [ ] Run `uv run nzlc sync --seed-work-ids seeds/work_ids.txt --max-works 5`.
- [ ] Run `uv run nzlc validate`.
- [ ] Run `uv run nzlc manifest`.
- [ ] Run `uv run nzlc coverage-report`.
- [ ] Inspect `data/_state/sync_state.json`, `data/manifests/latest_manifest.json`, and `data/manifests/latest_changes.json`.
