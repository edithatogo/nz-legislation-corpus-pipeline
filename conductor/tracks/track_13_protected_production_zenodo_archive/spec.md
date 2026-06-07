# Spec - Protected Production Zenodo Archive

## Status
blocked

## Goal
publish annual DOI snapshots only after explicit approval.

## Acceptance Criteria
- Production draft path is proven.
- Publication requires approval.
- DOI is recorded after publication.

## Evidence to Record
- Production deposition URL.
- DOI.
- Commit updating citation files.

## Evidence Recorded

- Local environment presence check on 2026-06-07:
  - `ZENODO_TOKEN`: absent.
  - `ZENODO_API_URL`: absent.
  - `ZENODO_DEPOSITION_ID`: absent.
  - `ARCHIVE_CREATORS_JSON`: absent.
  - `ARCHIVE_PUBLISH`: absent.
  - `GITHUB_REPOSITORY`: absent.
  - `GH_TOKEN`: absent.
  - `HF_REPO_ID`: absent.
- Local repository check on 2026-06-07:
  - No Git remote is configured.
  - The `zenodo-production` environment cannot be inspected or configured live.
- Local doctor command on 2026-06-07:
  - Command: `uv run --no-cache nzlc doctor`.
  - `ZENODO_TOKEN`: warning, not configured.
  - `ARCHIVE_CREATORS_JSON`: warning, not configured.
  - `HF_REPO_ID`: warning, not configured.
  - `output_dir`: `data`.
- Workflow and bootstrap evidence:
  - `.github/workflows/annual_zenodo_archive.yml` sends scheduled annual runs and manual `use_sandbox=false` runs to the `zenodo-production` environment.
  - The workflow defaults `publish` to `false`; publication requires explicit `publish=true`.
  - `scripts/bootstrap_github.sh --protect-production` attempts to configure `zenodo-production` with the authenticated user as required reviewer.
  - `docs/maintenance_runbook.md` requires production draft review before rerunning with `publish=true`.
- Production result:
  - No production draft was created.
  - No production deposition URL exists.
  - No DOI exists.
  - No citation commit was made.

## Blocked Items

- Cannot confirm `zenodo-production` required reviewers until a GitHub repository exists and environment settings are inspected.
- Cannot confirm environment-scoped production `ZENODO_TOKEN` until Track 02/GitHub environment configuration is complete.
- Cannot run production draft with `publish=false` until Track 12 sandbox archive passes and the production token/environment are configured.
- Cannot publish or record DOI until a reviewed production draft exists, reviewer approval is enforced, and `publish=true` is explicitly requested.
