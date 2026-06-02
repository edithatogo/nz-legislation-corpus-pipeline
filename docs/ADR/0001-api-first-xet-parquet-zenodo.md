# ADR 0001 — API-first, Hugging Face/Xet live hub, Zenodo annual archive

## Status

Accepted for initial implementation.

## Context

The corpus is expected to be large and evolving. GitHub is not a good place to store multi-GB mutable data. Researchers need both a live machine-readable corpus and fixed citable snapshots.

## Decision

Use:

- official New Zealand Legislation API for source intake
- optimized Parquet as the primary user-facing format
- Hugging Face Datasets/Xet as the live hub
- Zenodo as the annual DOI archive
- OSF only as an optional mirror

## Consequences

Positive:

- low daily bandwidth
- reproducible annual snapshots
- good downstream ML/data-science ergonomics
- GitHub repo remains small

Negative:

- corpus completeness depends on API discovery strategy
- first bootstrap may still take time
- Zenodo upload must be sandbox-tested
