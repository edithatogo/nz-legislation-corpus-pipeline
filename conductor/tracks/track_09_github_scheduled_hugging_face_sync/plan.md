# Plan - GitHub Scheduled Hugging Face Sync

## Tasks
- [ ] Confirm `.github/workflows/hf_sync.yml` exists on the default branch.
- [ ] Configure GitHub secrets and variables from Track 02.
- [ ] Run workflow manually with `max_works=5` and `min_seconds_between_requests=1.0`.
- [ ] Run workflow manually without `max_works` only after Track 07 and Track 08 are proven.
- [ ] Confirm scheduled daily runs restore Hugging Face state before syncing.
- [ ] Confirm workflow uploads only changed content.
- [ ] Confirm GitHub Actions summary includes sync state and latest changes.
