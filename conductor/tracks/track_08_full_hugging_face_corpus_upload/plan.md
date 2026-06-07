# Plan - Full Hugging Face Corpus Upload

## Tasks
- [ ] Confirm `HF_XET_HIGH_PERFORMANCE=1` for the upload environment.
- [ ] Run `uv run nzlc hf-upload`.
- [ ] Use resumable upload behavior if the upload is interrupted.
- [ ] Verify Hugging Face contains `parquet/`, `raw_xml/`, `records.jsonl`, `manifests/`, and `_state/` as expected.
- [ ] Re-download the dataset into a clean location and compare manifest hashes.
- [ ] Confirm the dataset card states the discovery and coverage status accurately.

## Current blocker

- `HF_TOKEN` is not configured in the local environment.
- `HF_REPO_ID` is not configured in the local environment.
- `data/`, `data/manifests/latest_manifest.json`, and `data/parquet/` are absent, so there is no full validated corpus ready for upload.
- Track 07 must complete first to produce the full local corpus and manifest.
- The upload helper defaults `HF_XET_HIGH_PERFORMANCE=1`, but the upload environment cannot be exercised until the corpus and credentials exist.
