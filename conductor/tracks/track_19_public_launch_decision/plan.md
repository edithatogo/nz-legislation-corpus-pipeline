# Plan - Public Launch Decision

## Tasks
- [ ] Confirm Tracks 01 through 14 are done or explicitly waived. Blocked: Tracks 02-14 still have unresolved blockers.
- [ ] Confirm Hugging Face contains the full intended live corpus or clearly labels the dataset as partial. Blocked until Track 03/08 publish or confirm the live dataset.
- [ ] Confirm GitHub scheduled sync is enabled and has passed after the first upload. Blocked until Track 09 runs on a configured GitHub repository.
- [ ] Confirm Zenodo sandbox archive has passed. Blocked until Track 12 passes.
- [x] Confirm public README, dataset card, and citation files match the actual coverage state.
- [x] Create a release note summarizing coverage, caveats, update cadence, and archival plan.

## Implementation Notes
- Added `docs/public_launch_decision.md` with a current `do not launch yet` decision, launch gates, final checklist, evidence fields, and rationale.
- Added `docs/public_launch_release_note.md` as a draft release note template that must be filled with live evidence before publication.
- Linked the launch gate from `README.md` and `docs/maintenance_runbook.md`.
- Reviewed current public wording in `README.md`, `DATASET_CARD.md`, and `CITATION.cff`; it keeps coverage as not proven complete and avoids claiming an annual Zenodo DOI exists.
- Launch remains blocked because credentials, final GitHub remote/repo, Hugging Face publication, full/bootstrap or partial-scope evidence, scheduled sync, and Zenodo sandbox archive are not proven.
