# Plan - Protected Production Zenodo Archive

## Tasks
- [ ] Configure `zenodo-production` GitHub environment with required reviewers.
- [ ] Confirm production `ZENODO_TOKEN` is environment-scoped.
- [ ] Run annual workflow with `publish=false` first.
- [ ] Review production draft metadata, license, creators, related identifiers, and files.
- [ ] Publish only after reviewer approval and explicit `publish=true`.
- [ ] Record DOI in `CITATION.cff`, `DATASET_CARD.md`, and Hugging Face dataset card.
