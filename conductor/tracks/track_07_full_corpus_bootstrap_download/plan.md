# Plan - Full Corpus Bootstrap Download

## Tasks
- [ ] Confirm enough local disk space for raw files, Parquet, manifests, and temporary archive work.
- [ ] Restore current Hugging Face corpus state into `data/` if any previous upload exists.
- [ ] Run full seed sync with `NZLC_MIN_SECONDS_BETWEEN_REQUESTS` set conservatively.
- [ ] Use staged batches if the seed inventory is large or API limits are uncertain.
- [ ] Preserve sync state after each batch.
- [ ] Run `uv run nzlc validate`, `uv run nzlc manifest`, and `uv run nzlc coverage-report`.
- [ ] Review missing text, missing XML URLs, failed versions, and ephemeral identifiers.
