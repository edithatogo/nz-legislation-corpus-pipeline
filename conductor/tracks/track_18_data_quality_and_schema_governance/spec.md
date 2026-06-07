# Spec - Data Quality And Schema Governance

## Status
blocked

## Goal
prevent silent schema drift or degraded corpus quality after the first public upload.

## Acceptance Criteria
- Upload cannot proceed after blocking validation failures.
- Schema version is visible in records or manifests.
- Coverage metrics can be compared between runs.
- Public docs explain backward compatibility expectations.

## Evidence to Record
- Schema version.
- Validation report path.
- Fixture list.
- Coverage baseline.

## Current Evidence
- Schema version: `record_schema_version = "1.0"`.
- Validation report path: `data/manifests/validation_report.json`.
- Fixture list: `tests/fixtures/sample_legislation.xml`, `tests/fixtures/sample_legislation.html`, plus validation tests for missing text, missing XML URL, missing source format/metadata-only content, and ephemeral identifiers.
- Coverage metrics are written to `data/manifests/coverage_report.json` and appended to `data/manifests/coverage_history.jsonl`.
- Live coverage baseline remains blocked until the full corpus exists.
