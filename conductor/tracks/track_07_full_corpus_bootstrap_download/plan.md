# Plan - Full Corpus Bootstrap Download

## Tasks
- [ ] Confirm enough local disk space for raw files, Parquet, manifests, and temporary archive work.
- [ ] Restore current Hugging Face corpus state into `data/` if any previous upload exists.
- [ ] Run full seed sync with `NZLC_MIN_SECONDS_BETWEEN_REQUESTS` set conservatively.
- [ ] Use staged batches if the seed inventory is large or API limits are uncertain.
- [ ] Preserve sync state after each batch.
- [ ] Run `uv run nzlc validate`, `uv run nzlc manifest`, and `uv run nzlc coverage-report`.
- [ ] Review missing text, missing XML URLs, failed versions, and ephemeral identifiers.

## Current blocker

- `NZ_LEGISLATION_API_KEY` is not configured in the local environment.
- `HF_TOKEN` and `HF_REPO_ID` are not configured, so no prior Hugging Face corpus state can be restored.
- `seeds/work_ids.txt` does not exist; only example seed files are present.
- `data/` is absent, and Tracks 05 and 06 have not produced a smoke corpus or upload proof.
- Local `C:` free space was checked at 19,907,948,544 bytes, but adequacy for the full corpus and temporary archive staging cannot be confirmed until the expected corpus size is known.
