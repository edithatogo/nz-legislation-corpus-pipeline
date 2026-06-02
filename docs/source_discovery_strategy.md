# Source discovery strategy

The source-of-truth ingestion path is the official New Zealand Legislation API. However, search-based discovery is not the same as proven full coverage.

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

Until a seed list or official full inventory is wired in, the project should describe itself as an automated corpus pipeline, not a proven complete corpus.
