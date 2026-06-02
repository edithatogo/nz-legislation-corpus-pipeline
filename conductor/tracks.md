# Project Tracks

This file tracks the major work items for `nz-legislation-corpus`.

---

## Status Key

- `todo`: not started.
- `blocked`: waiting on credentials, external access, or a decision.
- `ready`: prerequisites are available and implementation can proceed.
- `in_progress`: actively being worked.
- `done`: acceptance criteria are met and evidence is recorded.

## Track 01 - Repository Commit And Release Baseline

Status: `done`

Goal: get the current local implementation into a clean Git baseline before any live data operation is treated as repeatable.

Actions:

- Resolve the parent `OneDrive - Flinders` Git root lock issue or move `corpus-law-nz` into an isolated Git repository.
- Commit the currently staged rate-limit hardening, bootstrap guardrails, tests, and documentation.
- Generate a clean `uv.lock` from the final repository root.
- Switch CI dependency installation to `uv sync --all-extras --frozen` after `uv.lock` exists.
- Run `pytest -q -p no:cacheprovider tests`.
- Run `ruff check src/nz_legislation_corpus tests`.

Acceptance criteria:

- Git history contains a commit for the rate-limit work.
- `uv.lock` is committed.
- Tests and lint pass from the clean checkout.

Evidence to record:

- Commit SHA.
- Test command output summary.
- Lint command output summary.

## Track 02 - Credential And Secret Inventory

Status: `blocked`

Goal: confirm all credentials and GitHub variables required for live corpus operations are present, scoped correctly, and stored in the right place.

Actions:

- Confirm `NZ_LEGISLATION_API_KEY` exists and can call the NZ Legislation API.
- Confirm `HF_TOKEN` exists and has write access only to the intended Hugging Face dataset repository where possible.
- Confirm `HF_REPO_ID` is final.
- Confirm `ZENODO_TOKEN` exists for sandbox first.
- Decide whether production Zenodo uses a separate token and required reviewer environment.
- Store GitHub secrets: `NZ_LEGISLATION_API_KEY`, `HF_TOKEN`, and `ZENODO_TOKEN`.
- Store GitHub variables: `HF_REPO_ID`, `NZLC_SEARCH_TERMS`, `NZLC_SEARCH_FIELD`, `NZLC_SEARCH_SORT_BY`, `NZLC_LEGISLATION_TYPES`, `ARCHIVE_CREATORS_JSON`, and archive metadata.
- Run `uv run nzlc doctor` locally or through GitHub Actions.

Acceptance criteria:

- `nzlc doctor` passes without exposing secret values.
- GitHub Actions has the required secrets and variables.
- Zenodo production publication remains approval-gated.

Evidence to record:

- Redacted `nzlc doctor` result.
- GitHub repository variable names, not values.
- GitHub environment names and protection status.

## Track 03 - Hugging Face Dataset Shell

Status: `todo`

Goal: create and verify the Hugging Face dataset repository before uploading corpus data.

Actions:

- Create or confirm the Hugging Face dataset repository named by `HF_REPO_ID`.
- Run `scripts/create_huggingface_dataset_repo.sh "$HF_REPO_ID"` or equivalent API setup.
- Confirm the remote layout is root-based, not nested under `data/`.
- Confirm `.gitattributes`, dataset card metadata, and lightweight root placeholders are correct.
- Remove any legacy `data/...` placeholders if present.

Acceptance criteria:

- Hugging Face repo exists and is writable by the configured token.
- Root-level layout is ready for `parquet/`, `raw_xml/`, `manifests/`, and `_state/`.
- Dataset card describes live corpus status without claiming full coverage before discovery proof.

Evidence to record:

- Hugging Face repo URL.
- Root layout listing.
- Dataset card revision or commit hash.

## Track 04 - Source Discovery Completeness

Status: `todo`

Goal: establish the discovery method needed before the project can claim a complete corpus.

Actions:

- Contact or check the NZ Legislation source for an official work ID export or complete inventory.
- If no official export is available, build `seeds/work_ids.txt` from a documented authoritative inventory.
- Keep comments and provenance in the seed file or adjacent documentation.
- Reconcile seed coverage against search-based discovery.
- Define expected counts by legislation type, status, and year where available.
- Document any known exclusions, ephemeral IDs, or incorporated-by-reference caveats.

Acceptance criteria:

- `seeds/work_ids.txt` or an equivalent documented inventory exists.
- `docs/source_discovery_strategy.md` states the actual discovery source used.
- Public docs distinguish pipeline completeness from proven corpus completeness.

Evidence to record:

- Seed source.
- Work ID count.
- Reconciliation notes and unresolved gaps.

## Track 05 - Conservative Live Smoke Sync

Status: `todo`

Goal: prove the live sync path against external services without risking rate limits or large uploads.

Actions:

- Set `NZLC_MIN_SECONDS_BETWEEN_REQUESTS=1.0`.
- Run `uv run nzlc sync --seed-work-ids seeds/work_ids.txt --max-works 5`.
- Run `uv run nzlc validate`.
- Run `uv run nzlc manifest`.
- Run `uv run nzlc coverage-report`.
- Inspect `data/_state/sync_state.json`, `data/manifests/latest_manifest.json`, and `data/manifests/latest_changes.json`.

Acceptance criteria:

- Five or fewer seed works are synced exactly as requested.
- Validation passes.
- Manifest and coverage report are generated.
- No rate-limit failures are unhandled.

Evidence to record:

- Command summaries.
- Synced work count.
- Any API warnings from sync state.

## Track 06 - First Hugging Face Smoke Upload

Status: `todo`

Goal: prove upload, restore, and no-change behavior on Hugging Face with the small smoke corpus.

Actions:

- Run `uv run nzlc hf-upload` against the smoke data.
- Download the Hugging Face dataset back into a clean local `data/` directory.
- Confirm root-level remote files map to local `data/parquet/`, `data/raw_xml/`, `data/manifests/`, and `data/_state/`.
- Rerun upload with unchanged content and confirm it skips or produces no content churn.
- Inspect the Hugging Face dataset viewer and sample Parquet reads.

Acceptance criteria:

- Smoke corpus is visible in Hugging Face.
- Re-download produces the expected local layout.
- No-change upload behavior is proven.

Evidence to record:

- Hugging Face commit or revision.
- Manifest hash before and after no-change upload.
- Sample Parquet read result.

## Track 07 - Full Corpus Bootstrap Download

Status: `todo`

Goal: download the full corpus into local `data/` using the proven discovery method and conservative pacing.

Actions:

- Confirm enough local disk space for raw files, Parquet, manifests, and temporary archive work.
- Restore current Hugging Face corpus state into `data/` if any previous upload exists.
- Run full seed sync with `NZLC_MIN_SECONDS_BETWEEN_REQUESTS` set conservatively.
- Use staged batches if the seed inventory is large or API limits are uncertain.
- Preserve sync state after each batch.
- Run `uv run nzlc validate`, `uv run nzlc manifest`, and `uv run nzlc coverage-report`.
- Review missing text, missing XML URLs, failed versions, and ephemeral identifiers.

Acceptance criteria:

- All seed works are attempted.
- Failed versions are recorded and triaged.
- Validation passes or documented exceptions are accepted.
- Coverage report is reviewed before any public completeness claim.

Evidence to record:

- Total works attempted.
- Total versions and records produced.
- Failed or skipped version list.
- Final manifest hash.
- Coverage report path.

## Track 08 - Full Hugging Face Corpus Upload

Status: `todo`

Goal: publish the full validated corpus to Hugging Face as the live operational dataset.

Actions:

- Confirm `HF_XET_HIGH_PERFORMANCE=1` for the upload environment.
- Run `uv run nzlc hf-upload`.
- Use resumable upload behavior if the upload is interrupted.
- Verify Hugging Face contains `parquet/`, `raw_xml/`, `records.jsonl`, `manifests/`, and `_state/` as expected.
- Re-download the dataset into a clean location and compare manifest hashes.
- Confirm the dataset card states the discovery and coverage status accurately.

Acceptance criteria:

- Full corpus upload completes.
- Re-downloaded manifest matches the uploaded manifest.
- Dataset card and README do not overclaim completeness.

Evidence to record:

- Hugging Face revision or commit hash.
- Uploaded size.
- Manifest hash.
- Re-download verification result.

## Track 09 - GitHub Scheduled Hugging Face Sync

Status: `todo`

Goal: make GitHub Actions the normal maintenance loop for the Hugging Face live corpus.

Actions:

- Confirm `.github/workflows/hf_sync.yml` exists on the default branch.
- Configure GitHub secrets and variables from Track 02.
- Run workflow manually with `max_works=5` and `min_seconds_between_requests=1.0`.
- Run workflow manually without `max_works` only after Track 07 and Track 08 are proven.
- Confirm scheduled daily runs restore Hugging Face state before syncing.
- Confirm workflow uploads only changed content.
- Confirm GitHub Actions summary includes sync state and latest changes.

Acceptance criteria:

- Manual smoke workflow passes.
- Full manual workflow passes.
- Daily scheduled workflow is enabled and uses the Hugging Face repo as the live data hub.

Evidence to record:

- GitHub Actions run URLs.
- Workflow inputs used.
- Latest successful scheduled run URL.

## Track 10 - Maintenance Doctor And Alerting

Status: `todo`

Goal: surface token, API, and dependency failures before they affect the live corpus.

Actions:

- Enable `.github/workflows/doctor.yml`.
- Confirm doctor runs without mutating corpus data.
- Confirm GitHub Actions notifications reach the maintainer.
- Decide whether to add a lightweight webhook or issue creation on repeated failures.
- Review Dependabot configuration and security workflows.

Acceptance criteria:

- Doctor workflow passes once with live secrets.
- Failure notification path is known.
- Maintainer has a weekly check routine.

Evidence to record:

- Doctor workflow run URL.
- Notification destination.
- Any follow-up alerting issue.

## Track 11 - Monthly Full Reconciliation

Status: `todo`

Goal: keep the corpus complete over time, not only during the first bootstrap.

Actions:

- Define a monthly or quarterly full reconciliation cadence.
- Compare seed inventory, search discovery, and coverage report outputs.
- Add newly discovered work IDs to `seeds/work_ids.txt` with provenance.
- Rerun full sync in staged batches when the seed file changes materially.
- Review counts by legislation type, status, and year.

Acceptance criteria:

- Reconciliation cadence is documented.
- Seed changes are reviewed.
- Coverage deltas are explained in `latest_changes.json` or a maintenance note.

Evidence to record:

- Reconciliation date.
- Added or removed work IDs.
- Coverage deltas.

## Track 12 - Zenodo Sandbox Archive

Status: `todo`

Goal: prove annual immutable archiving without publishing to production.

Actions:

- Set Zenodo sandbox token and sandbox API URL.
- Run `uv run nzlc archive --year <year> --output-dir dist/archive`.
- Run `uv run nzlc zenodo-upload --year <year> --archive-dir dist/archive` against sandbox.
- Verify archive manifest and checksums.
- Verify duplicate-file replacement behavior if rerun.

Acceptance criteria:

- Sandbox draft is created or updated.
- Archive, manifest, and checksum files are present.
- No production publication occurs.

Evidence to record:

- Sandbox deposition URL.
- Archive filename and checksum.
- Workflow run URL if performed in GitHub Actions.

## Track 13 - Protected Production Zenodo Archive

Status: `todo`

Goal: publish annual DOI snapshots only after explicit approval.

Actions:

- Configure `zenodo-production` GitHub environment with required reviewers.
- Confirm production `ZENODO_TOKEN` is environment-scoped.
- Run annual workflow with `publish=false` first.
- Review production draft metadata, license, creators, related identifiers, and files.
- Publish only after reviewer approval and explicit `publish=true`.
- Record DOI in `CITATION.cff`, `DATASET_CARD.md`, and Hugging Face dataset card.

Acceptance criteria:

- Production draft path is proven.
- Publication requires approval.
- DOI is recorded after publication.

Evidence to record:

- Production deposition URL.
- DOI.
- Commit updating citation files.

## Track 14 - Legal, Citation, And Dataset Wording

Status: `todo`

Goal: keep public statements accurate about corpus coverage, licensing, and incorporated-by-reference material.

Actions:

- Review `README.md`, `DATASET_CARD.md`, `CITATION.cff`, and archive metadata.
- State whether discovery is complete, partial, seed-based, or search-based.
- Separate code license from legislation reuse status.
- Add caveats for incorporated-by-reference material and non-legislative website content.
- Confirm citation guidance for Hugging Face live data and Zenodo annual snapshots.

Acceptance criteria:

- Public docs make no unsupported completeness claim.
- License and citation wording are internally consistent.
- Zenodo and Hugging Face metadata align.

Evidence to record:

- Reviewed files.
- Reviewer notes.
- Metadata commit SHA.

## Track 15 - Downstream Researcher Usability

Status: `todo`

Goal: make the published corpus easy to inspect and query after the live hub is stable.

Actions:

- Add a small public sample split if useful for users who do not want the full corpus.
- Add DuckDB or Polars examples that query Parquet directly from Hugging Face.
- Add a minimal data dictionary from schema fields.
- Optionally add a Hugging Face Space for browsing/search after core maintenance is stable.

Acceptance criteria:

- A new user can query the Parquet dataset without downloading the full raw corpus.
- Examples are tested or manually verified.
- Optional browser UI is clearly secondary to the dataset pipeline.

Evidence to record:

- Example command output.
- Sample dataset path or revision.
- Documentation links.

## Track 16 - GitHub Repository Hardening

Status: `todo`

Goal: make the GitHub repository safe to operate as the automation controller for the live Hugging Face corpus.

Actions:

- Create or confirm the final GitHub repository.
- Push the code-only repository without `data/`, `dist/`, cache directories, or generated corpus files.
- Enable branch protection on the default branch.
- Require the tests workflow before merge once CI is stable.
- Enable secret scanning and push protection where available.
- Enable Dependabot alerts and dependency update PRs.
- Confirm `CODEOWNERS`, issue templates, pull request template, security policy, and contribution docs are present if the repo is public.
- Confirm workflows have minimum permissions and do not expose secrets in logs.

Acceptance criteria:

- Default branch is protected.
- Tests are required for code changes.
- Secret scanning and dependency alerts are enabled or explicitly documented as unavailable.
- Repository remains code-only.

Evidence to record:

- GitHub repository URL.
- Branch protection summary.
- Enabled security settings.
- First passing CI run URL.

## Track 17 - Runtime Capacity, Batching, And Resume

Status: `todo`

Goal: make the full corpus bootstrap and recurring sync practical under local disk, GitHub Actions runtime, API rate limits, and upload interruption constraints.

Actions:

- Estimate disk required for raw files, normalized records, Parquet, manifests, and annual archive staging.
- Decide whether first full bootstrap runs locally, on GitHub Actions, or on another controlled runner.
- Define batch size and pacing defaults for first full sync.
- Confirm sync state is preserved between batches.
- Confirm interrupted Hugging Face uploads can resume without corrupting the remote dataset.
- Add an operator note for cleaning local generated data safely after upload and verification.
- Record the fallback plan if the full bootstrap exceeds GitHub Actions timeout.

Acceptance criteria:

- Bootstrap runner and disk budget are documented.
- Batch/resume procedure is written and tested with a non-trivial batch.
- Generated local data cleanup is documented and does not affect Git-tracked files.

Evidence to record:

- Disk estimate.
- Chosen runner.
- Batch size and pacing values.
- Resume test result.

## Track 18 - Data Quality And Schema Governance

Status: `todo`

Goal: prevent silent schema drift or degraded corpus quality after the first public upload.

Actions:

- Define minimum validation checks required before upload.
- Define which validation warnings block upload and which are informational.
- Add or confirm fixture coverage for representative XML, HTML, missing-text, missing-format, and ephemeral-ID cases.
- Version the record schema explicitly before public release.
- Document how schema changes are migrated or announced.
- Track data-quality metrics from `coverage_report.json` over time.

Acceptance criteria:

- Upload cannot proceed after blocking validation failures.
- Schema version is visible in records or manifests.
- Coverage metrics can be compared between runs.
- Public docs explain backward compatibility expectations.

Evidence to record:

- Schema version.
- Validation report path.
- Fixture list.
- Coverage baseline.

## Track 19 - Public Launch Decision

Status: `todo`

Goal: make a deliberate launch decision after the corpus, automation, metadata, and maintenance loop are all proven.

Actions:

- Confirm Tracks 01 through 14 are done or explicitly waived.
- Confirm Hugging Face contains the full intended live corpus or clearly labels the dataset as partial.
- Confirm GitHub scheduled sync is enabled and has passed after the first upload.
- Confirm Zenodo sandbox archive has passed.
- Confirm public README, dataset card, and citation files match the actual coverage state.
- Create a release note summarizing coverage, caveats, update cadence, and archival plan.

Acceptance criteria:

- Public users can find the live dataset, source repository, coverage statement, and citation instructions.
- No public page claims full coverage unless Track 04 is proven.
- Maintainer has a clear monthly and annual operating checklist.

Evidence to record:

- Launch date.
- Hugging Face revision.
- GitHub release or tag.
- Final launch checklist.
