# Improvement backlog

Prioritized, low-maintenance improvements after v0.3.

## P0 — Corpus completeness proof

The current API-first pipeline is correct structurally, but a complete legal corpus needs a reliable discovery source.

Preferred options:

1. Official bulk work ID export, if available from the NZ Legislation team.
2. A maintained seed list of work IDs checked into `seeds/work_ids.txt` or stored on Hugging Face if large.
3. Reconciliation against site maps or another authoritative inventory.
4. Search-term expansion only as a temporary discovery aid.

Do not claim full coverage until this is resolved.

## P0 — Protected Zenodo production workflow

Keep `publish=false` except for a reviewed annual snapshot. Use the `zenodo-production` environment with required reviewers before any production publication.

## P1 — Environment-scoped secrets

Move `ZENODO_TOKEN` from repository secrets to environment secrets once the repo is stable. Daily sync does not need Zenodo access.

## P1 — Synthetic monitoring

Implemented in `.github/workflows/doctor.yml`. Keep it enabled so token/API failures are surfaced without mutating data.

## P1 — Stronger archival provenance

Add GitHub artifact attestations or a SLSA-style provenance JSON for annual archives.

## P2 — Formal schema versioning

Add explicit migration scripts if the record schema changes.

## P2 — Automated changelog publishing

Publish `latest_changes.json` summaries as Hugging Face commit notes or GitHub workflow summaries.

## P2 — DuckDB/Polars examples

Add notebooks that query the Parquet dataset directly from Hugging Face.
