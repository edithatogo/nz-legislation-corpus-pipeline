# Plan - Data Quality And Schema Governance

## Tasks
- [x] Define minimum validation checks required before upload.
- [x] Define which validation warnings block upload and which are informational.
- [x] Add or confirm fixture coverage for representative XML, HTML, missing-text, missing-format, and ephemeral-ID cases.
- [x] Version the record schema explicitly before public release.
- [x] Document how schema changes are migrated or announced.
- [x] Track data-quality metrics from `coverage_report.json` over time.

## Implementation Notes
- Added `record_schema_version = "1.0"` to normalized records and `schemas/legislation_record.schema.json`.
- Added `src/nz_legislation_corpus/schema.py` as the single local version constant.
- Added `record_schema` and `record_schema_version` to generated manifests.
- `nzlc hf-upload` now runs validation before creating or uploading to the Hugging Face dataset and aborts on blocking validation errors.
- `validate_records` now reports blocking error types and informational warning types; missing XML URLs and ephemeral identifiers are informational.
- Added `docs/schema_governance.md` and linked it from README and the maintenance runbook.
- Added `tests/fixtures/sample_legislation.html` and expanded tests for XML, HTML, missing text, missing XML URL, ephemeral IDs, and pre-upload validation blocking.
- `nzlc coverage-report` now appends current metrics to `data/manifests/coverage_history.jsonl`.
- Live baseline coverage remains blocked until Track 07/08 produce and publish the real corpus.
