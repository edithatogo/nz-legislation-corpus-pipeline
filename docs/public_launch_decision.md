# Public launch decision

Decision status: do not launch yet.

Decision date: 2026-06-07.

## Launch gate

Public launch requires every gate below to be satisfied or explicitly waived in writing.

| Gate | Current status | Evidence required |
| --- | --- | --- |
| Tracks 01-14 done or explicitly waived | Blocked | Track status review showing no unresolved blockers, or dated waiver for each blocker. |
| Hugging Face live dataset exists | Blocked | Dataset URL, revision, manifest hash, and sample Parquet read. |
| Dataset scope is accurate | Blocked | Track 04 source-discovery evidence or public partial-scope wording retained everywhere. |
| First full or intentionally partial corpus uploaded | Blocked | Upload run URL, `manifests/latest_manifest.json`, and re-download/query proof. |
| GitHub scheduled sync enabled and passing | Blocked | `hf_sync.yml` run URL after first upload and scheduled-run confirmation. |
| Zenodo sandbox archive passed | Blocked | Sandbox draft URL, archive filename, manifest, and checksum. |
| Public README, dataset card, and citation files match actual coverage | Ready for current prelaunch state | README, dataset card, and citation text currently state coverage is not proven complete and avoid fixed DOI claims. Recheck after live corpus publication. |
| Monthly and annual operating checklist exists | Ready locally | `docs/maintenance_runbook.md`, `docs/reconciliation_runbook.md`, `docs/runtime_capacity_runbook.md`, and `docs/schema_governance.md`. |

## Final launch checklist

Before changing this decision to launch:

1. Confirm `conductor/tracks.md` shows Tracks 01-14 as `done` or has dated waiver notes for each blocker.
2. Record the GitHub repository URL and release/tag.
3. Record the Hugging Face dataset URL, revision, and manifest hash.
4. Run a sample Hugging Face Parquet read and save the output path or query result.
5. Confirm `hf_sync.yml` has passed after the first upload.
6. Confirm the weekly doctor workflow has passed.
7. Confirm the Zenodo sandbox archive has passed and checksums match.
8. Re-read `README.md`, `DATASET_CARD.md`, and `CITATION.cff` against the actual coverage state.
9. Keep full-coverage language out of all public pages unless Track 04 is proven.
10. Update `docs/public_launch_release_note.md` with the real URLs, dates, manifest hash, coverage count, and archive evidence.

## Evidence fields to fill at launch

```text
Launch date:
GitHub repository URL:
GitHub release or tag:
Hugging Face dataset URL:
Hugging Face revision:
Manifest hash:
Coverage statement:
Record count:
First passing scheduled sync URL:
Doctor workflow URL:
Zenodo sandbox archive URL:
Zenodo production DOI, if any:
Final reviewer:
```

## Current rationale

Launching now would overstate operational readiness. The local code and documentation are close to launch-ready, but the external corpus publication path is not proven: credentials are missing, no GitHub remote is configured, the Hugging Face dataset has not been verified, the full corpus has not been bootstrapped, scheduled sync has not run, and Zenodo sandbox archival has not passed.
