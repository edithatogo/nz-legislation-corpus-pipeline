# Spec - GitHub Scheduled Hugging Face Sync

## Status
blocked

## Goal
make GitHub Actions the normal maintenance loop for the Hugging Face live corpus.

## Acceptance Criteria
- Manual smoke workflow passes.
- Full manual workflow passes.
- Daily scheduled workflow is enabled and uses the Hugging Face repo as the live data hub.

## Evidence to Record
- GitHub Actions run URLs.
- Workflow inputs used.
- Latest successful scheduled run URL.

## Evidence Recorded

- Local workflow check on 2026-06-07:
  - `.github/workflows/hf_sync.yml`: present.
  - The workflow has a daily schedule: `17 14 * * *`.
  - The workflow has `workflow_dispatch` inputs for `latest_only`, `max_works`, and `min_seconds_between_requests`.
  - The workflow restores the current live corpus from Hugging Face before sync.
  - The workflow runs `uv run nzlc sync`, `uv run nzlc validate`, `uv run nzlc manifest`, `uv run nzlc coverage-report`, and `uv run nzlc hf-upload`.
  - The upload step sets `HF_XET_HIGH_PERFORMANCE: "1"`.
  - The step summary includes `data/_state/sync_state.json` and `data/manifests/latest_changes.json` when present.
- Local repository check on 2026-06-07:
  - No Git remote is configured.
  - There is no locally resolvable target GitHub repository/default branch for Actions dispatch.
- Local environment presence check on 2026-06-07:
  - `GITHUB_REPOSITORY`: absent.
  - `GH_TOKEN`: absent.
  - `NZ_LEGISLATION_API_KEY`: absent.
  - `HF_TOKEN`: absent.
  - `HF_REPO_ID`: absent.
- Local doctor command on 2026-06-07:
  - Command: `uv run --no-cache nzlc doctor`.
  - `NZ_LEGISLATION_API_KEY`: warning, not configured.
  - `HF_REPO_ID`: warning, not configured.
  - `HF_TOKEN`: warning, not configured.
  - `output_dir`: `data`.

## Blocked Items

- Cannot confirm `.github/workflows/hf_sync.yml` exists on the default branch until a GitHub remote/repository is configured and pushed.
- Cannot configure or verify GitHub secrets/variables until Track 02 is unblocked.
- Cannot run the manual smoke workflow until GitHub Actions is available and required secrets/variables exist.
- Cannot run the full manual workflow until Tracks 07 and 08 are proven.
- Cannot confirm scheduled daily runs, changed-content behavior, or successful Actions summaries until the workflow has run in GitHub.
