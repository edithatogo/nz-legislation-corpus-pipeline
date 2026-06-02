# Synthesised and prioritised recommendations

## P0 — Must do before public launch

1. Obtain and store `NZ_LEGISLATION_API_KEY`, `HF_TOKEN`, and `ZENODO_TOKEN` as GitHub secrets.
2. Create a Hugging Face dataset repository and set `HF_REPO_ID` as a GitHub variable.
3. Establish corpus discovery completeness: use a seed work-ID file, official bulk source, or an agreed search strategy.
4. Run `annual_zenodo_archive.yml` against Zenodo sandbox before production.
5. Verify legal/citation wording, especially incorporated-by-reference material.

## P1 — Strongly recommended

1. Keep Parquet writer options stable.
2. Run daily latest-only sync plus less frequent full reconciliation.
3. Add alerting via GitHub Actions notifications or a lightweight webhook.
4. Add structural XML extraction after the plain-text corpus is stable.
5. Add a data-quality dashboard from validation reports.

## P2 — Nice to have

1. Add DuckDB examples for downstream researchers.
2. Add a Hugging Face Space for browsing/search.
3. Add OSF mirror only if you need it, with archive splitting.
4. Add `CITATION.cff` updates after the first Zenodo DOI is minted.
