# Spec - Credential And Secret Inventory

## Status
blocked

## Goal
confirm all credentials and GitHub variables required for live corpus operations are present, scoped correctly, and stored in the right place.

## Acceptance Criteria
- `nzlc doctor` passes without exposing secret values.
- GitHub Actions has the required secrets and variables.
- Zenodo production publication remains approval-gated.

## Evidence to Record
- Redacted `nzlc doctor` result.
- GitHub repository variable names, not values.
- GitHub environment names and protection status.
