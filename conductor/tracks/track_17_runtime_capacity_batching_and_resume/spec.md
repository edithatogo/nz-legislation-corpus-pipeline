# Spec - Runtime Capacity, Batching, And Resume

## Status
todo

## Goal
make the full corpus bootstrap and recurring sync practical under local disk, GitHub Actions runtime, API rate limits, and upload interruption constraints.

## Acceptance Criteria
- Bootstrap runner and disk budget are documented.
- Batch/resume procedure is written and tested with a non-trivial batch.
- Generated local data cleanup is documented and does not affect Git-tracked files.

## Evidence to Record
- Disk estimate.
- Chosen runner.
- Batch size and pacing values.
- Resume test result.
