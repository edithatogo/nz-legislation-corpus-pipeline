# Plan - Protected Production Zenodo Archive

## Tasks
- [ ] Configure `zenodo-production` GitHub environment with required reviewers.
- [ ] Confirm production `ZENODO_TOKEN` is environment-scoped.
- [ ] Run annual workflow with `publish=false` first.
- [ ] Review production draft metadata, license, creators, related identifiers, and files.
- [ ] Publish only after reviewer approval and explicit `publish=true`.
- [ ] Record DOI in `CITATION.cff`, `DATASET_CARD.md`, and Hugging Face dataset card.

## Current blocker

- No Git remote is configured, so `zenodo-production` cannot be configured or verified live.
- `ZENODO_TOKEN`, `ARCHIVE_CREATORS_JSON`, `GITHUB_REPOSITORY`, `GH_TOKEN`, and `HF_REPO_ID` are not configured in the local environment.
- Track 12 sandbox archive has not passed; production Zenodo work should not proceed before sandbox proof.
- The annual workflow and bootstrap script contain the intended approval gate, but no production draft, approval, DOI, or citation update can be produced yet.
