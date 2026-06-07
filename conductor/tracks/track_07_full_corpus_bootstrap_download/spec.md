# Spec - Full Corpus Bootstrap Download

## Status
blocked

## Goal
download the full corpus into local `data/` using the proven discovery method and conservative pacing.

## Acceptance Criteria
- All seed works are attempted.
- Failed versions are recorded and triaged.
- Validation passes or documented exceptions are accepted.
- Coverage report is reviewed before any public completeness claim.

## Evidence to Record
- Total works attempted.
- Total versions and records produced.
- Failed or skipped version list.
- Final manifest hash.
- Coverage report path.

## Evidence Recorded

- Local environment presence check on 2026-06-07:
  - `NZ_LEGISLATION_API_KEY`: absent.
  - `HF_TOKEN`: absent.
  - `HF_REPO_ID`: absent.
  - `NZLC_MIN_SECONDS_BETWEEN_REQUESTS`: absent.
  - `NZLC_OUTPUT_DIR`: absent.
- Seed inventory check on 2026-06-07:
  - `seeds/work_ids.txt`: absent.
  - The checked-in seed files are examples only and not an authoritative inventory.
- Local data check on 2026-06-07:
  - `data/`: absent.
- Local doctor command on 2026-06-07:
  - Command: `uv run --no-cache nzlc doctor`.
  - `NZ_LEGISLATION_API_KEY`: warning, not configured.
  - `HF_REPO_ID`: warning, not configured.
  - `HF_TOKEN`: warning, not configured.
  - `output_dir`: `data`.
- Local disk check on 2026-06-07:
  - `C:` free space: 19,907,948,544 bytes.
  - Adequacy for raw files, Parquet, manifests, and temporary archive staging is not confirmed because the full corpus and archive size estimate is not known.
- Full bootstrap was not run because the prerequisites are absent and earlier smoke tracks have not completed.

## Blocked Items

- Cannot restore current Hugging Face corpus state until `HF_TOKEN` and `HF_REPO_ID` are configured and a dataset exists.
- Cannot run full seed sync until `NZ_LEGISLATION_API_KEY` and an authoritative `seeds/work_ids.txt` are available.
- Cannot preserve or inspect sync state, validation, manifest, coverage, failed-version, or final hash evidence until the full bootstrap starts from a valid seed inventory.
- Cannot confirm local disk adequacy until a full-corpus size estimate or staged bootstrap budget is established.
