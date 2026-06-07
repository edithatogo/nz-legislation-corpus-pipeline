# Plan - GitHub Scheduled Hugging Face Sync

## Tasks
- [x] Confirm `.github/workflows/hf_sync.yml` exists locally.
- [ ] Configure GitHub secrets and variables from Track 02.
- [ ] Run workflow manually with `max_works=5` and `min_seconds_between_requests=1.0`.
- [ ] Run workflow manually without `max_works` only after Track 07 and Track 08 are proven.
- [ ] Confirm scheduled daily runs restore Hugging Face state before syncing.
- [ ] Confirm workflow uploads only changed content.
- [ ] Confirm GitHub Actions summary includes sync state and latest changes.

## Current blocker

- `.github/workflows/hf_sync.yml` exists locally, but no Git remote is configured, so default-branch presence cannot be confirmed.
- `GITHUB_REPOSITORY` and `GH_TOKEN` are not configured in the local environment.
- `NZ_LEGISLATION_API_KEY`, `HF_TOKEN`, and `HF_REPO_ID` are not configured.
- Track 02 must configure GitHub secrets/variables before the workflow can run.
- Tracks 05, 07, and 08 must complete before smoke/full/no-change workflow behavior can be proven.
