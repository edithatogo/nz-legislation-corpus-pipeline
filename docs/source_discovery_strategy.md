# Source discovery strategy

The source-of-truth ingestion path is the official New Zealand Legislation API. However, public API documentation checked on 2026-06-07 describes the API as equivalent to the website search function; search-based discovery is not the same as proven full coverage.

See `docs/source_inventory_status.md` for the current inventory evidence and unresolved coverage blocker.

## Recommended approach

Use a three-layer discovery strategy:

1. **Seed list:** maintain `seeds/work_ids.txt` with known work IDs from an official source or manually verified export.
2. **API freshness search:** use `NZLC_SEARCH_SORT_BY=most_recently_updated` and broad search terms to catch new/changed works.
3. **Coverage reconciliation:** run `nzlc coverage-report` and compare counts by type/status/year against expected official totals where available.

## Seed file format

```text
# comments are allowed
act_public_1990_109
act_public_1993_82
```

Run:

```bash
uv run nzlc sync --seed-work-ids seeds/work_ids.txt
```

## Current risk rating

Until a seed list, official full inventory, or documented reconciliation is wired in, the project should describe itself as an automated corpus pipeline, not a proven complete corpus.
