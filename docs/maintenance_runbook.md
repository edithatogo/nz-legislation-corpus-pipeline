# Maintenance runbook

## Weekly

1. Check the `Non-destructive service doctor` workflow.
2. Check the latest `Hugging Face live sync` summary.
3. Merge safe Dependabot PRs after tests pass.

## Monthly

1. Review `coverage_report.json` in the Hugging Face dataset repo.
2. Run a manual sync with `max_works=20` if the daily sync has been mostly no-op.
3. Confirm Hugging Face upload skipped when content did not change.

## Quarterly

1. Review the NZ Legislation API docs for endpoint/rate-limit changes.
2. Refresh or reconcile `seeds/work_ids.txt` if available.
3. Review schema changes and deprecation warnings.

## Annual Zenodo archive

1. Run the annual workflow with `use_sandbox=true` and `publish=false`.
2. Verify archive checksums.
3. Run production draft with `use_sandbox=false` and `publish=false`.
4. Review the production draft on Zenodo.
5. Re-run with `publish=true` only after approval through the `zenodo-production` environment.
6. Store the published DOI in `CITATION.cff` and the Hugging Face dataset card.

## Incident response

### API failures

- Check whether the API key is valid.
- Rerun with `max_works=5` and `NZLC_MIN_SECONDS_BETWEEN_REQUESTS=1.0`.
- If 429/403 responses increased, reduce page size or schedule less frequently.

### Hugging Face upload failures

- Confirm `HF_TOKEN` has write access to `HF_REPO_ID`.
- Rerun; `hf upload-large-folder` is designed to resume large uploads.
- Check that generated local `data/` does not contain unexpected caches or temporary files.

### Zenodo failures

- Retry sandbox first.
- Never delete a published record.
- If a draft contains duplicate files, the uploader attempts to replace duplicate filenames before uploading.
