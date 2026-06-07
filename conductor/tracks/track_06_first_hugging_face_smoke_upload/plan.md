# Plan - First Hugging Face Smoke Upload

## Tasks
- [ ] Run `uv run nzlc hf-upload` against the smoke data.
- [ ] Download the Hugging Face dataset back into a clean local `data/` directory.
- [ ] Confirm root-level remote files map to local `data/parquet/`, `data/raw_xml/`, `data/manifests/`, and `data/_state/`.
- [ ] Rerun upload with unchanged content and confirm it skips or produces no content churn.
- [ ] Inspect the Hugging Face dataset viewer and sample Parquet reads.

## Current blocker

- `HF_TOKEN` is not configured in the local environment.
- `HF_REPO_ID` is not configured in the local environment.
- `data/` and `data/manifests/latest_manifest.json` are absent, so there is no smoke corpus ready for upload.
- Track 05 must complete first to produce the conservative live smoke data that this track uploads and verifies.
