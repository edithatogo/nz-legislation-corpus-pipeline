# Spec - Data Quality And Schema Governance

## Status
todo

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
