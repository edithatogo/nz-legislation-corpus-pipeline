# Plan - Runtime Capacity, Batching, And Resume

## Tasks
- [ ] Estimate disk required for raw files, normalized records, Parquet, manifests, and annual archive staging.
- [ ] Decide whether first full bootstrap runs locally, on GitHub Actions, or on another controlled runner.
- [ ] Define batch size and pacing defaults for first full sync.
- [ ] Confirm sync state is preserved between batches.
- [ ] Confirm interrupted Hugging Face uploads can resume without corrupting the remote dataset.
- [ ] Add an operator note for cleaning local generated data safely after upload and verification.
- [ ] Record the fallback plan if the full bootstrap exceeds GitHub Actions timeout.
