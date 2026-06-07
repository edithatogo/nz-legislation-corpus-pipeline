# Spec - Source Discovery Completeness

## Status
blocked

## Goal
establish the discovery method needed before the project can claim a complete corpus.

## Acceptance Criteria
- `seeds/work_ids.txt` or an equivalent documented inventory exists.
- `docs/source_discovery_strategy.md` states the actual discovery source used.
- Public docs distinguish pipeline completeness from proven corpus completeness.

## Evidence to Record
- Seed source.
- Work ID count.
- Reconciliation notes and unresolved gaps.

## Evidence Recorded

- Public source check on 2026-06-07:
  - Official API documentation describes `/v0/works` as search for works.
  - Official developer API page says the current API functionality is equivalent to the website search function.
  - No public complete work-ID export, bulk inventory endpoint, or modified-since enumeration endpoint was identified.
- Local repository inventory:
  - No authoritative `seeds/work_ids.txt` exists.
  - `seeds/work_ids.txt.example` and `seeds/work_ids.example.txt` are examples only.
  - `docs/source_inventory_status.md` records the current inventory status and unresolved blocker.
- Public wording:
  - `README.md` already warns against claiming complete coverage from search-based discovery.
  - `DATASET_CARD.md` now states that corpus completeness is not yet proven and requires reconciliation against an authoritative inventory.
  - `docs/source_discovery_strategy.md` now points to the current inventory evidence.

## Blocked Items

- Cannot build a provenance-backed `seeds/work_ids.txt` until an official export or authoritative inventory is obtained.
- Cannot reconcile seed coverage against search-based discovery until the seed inventory exists.
- Cannot define expected counts by type, status, and year without an authoritative count source or completed inventory.
