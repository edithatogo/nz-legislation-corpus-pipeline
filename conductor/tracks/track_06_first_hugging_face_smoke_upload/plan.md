# Plan - First Hugging Face Smoke Upload

## Tasks
- [ ] Run `uv run nzlc hf-upload` against the smoke data.
- [ ] Download the Hugging Face dataset back into a clean local `data/` directory.
- [ ] Confirm root-level remote files map to local `data/parquet/`, `data/raw_xml/`, `data/manifests/`, and `data/_state/`.
- [ ] Rerun upload with unchanged content and confirm it skips or produces no content churn.
- [ ] Inspect the Hugging Face dataset viewer and sample Parquet reads.
