# Plan - Full Hugging Face Corpus Upload

## Tasks
- [ ] Confirm `HF_XET_HIGH_PERFORMANCE=1` for the upload environment.
- [ ] Run `uv run nzlc hf-upload`.
- [ ] Use resumable upload behavior if the upload is interrupted.
- [ ] Verify Hugging Face contains `parquet/`, `raw_xml/`, `records.jsonl`, `manifests/`, and `_state/` as expected.
- [ ] Re-download the dataset into a clean location and compare manifest hashes.
- [ ] Confirm the dataset card states the discovery and coverage status accurately.
