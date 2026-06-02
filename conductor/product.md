# Product Context

## Product summary

`nz-legislation-corpus` is an API-first pipeline for building and maintaining a
New Zealand legislation corpus. It ingests data from the official NZ
Legislation API, normalizes records, preserves provenance, writes optimized
Parquet shards, and publishes the live corpus to Hugging Face Datasets with
annual archive snapshots on Zenodo.

## Primary users

- Maintainers operating the corpus pipeline.
- Researchers or downstream consumers who need a stable legislation dataset.
- CI/CD and release automation that validates, packages, and publishes corpus
  artifacts.

## Core goals

- Keep the repository code-only and easy to audit.
- Make sync, validation, manifest generation, and archive publication
  idempotent.
- Preserve source provenance for every record.
- Minimize upload churn by comparing stable content hashes and preserving
  unchanged records.
- Keep live dataset publishing and annual archiving reproducible and safe to
  rerun.

## Key capabilities

- Discover and sync legislation records from the official NZ Legislation API.
- Normalize legislation data into machine-friendly records.
- Extract and preserve raw XML or HTML provenance when available.
- Write partitioned Parquet shards for efficient downstream use.
- Generate manifests and checksums for auditability.
- Publish the live dataset to Hugging Face Datasets using Xet-aware uploads.
- Produce annual Zenodo archive bundles and draft deposits.
- Validate corpus state and coverage with deterministic local commands.

## Non-goals

- This repository is not a general legal analysis tool.
- It is not a manual curation interface for editing legislation content.
- It does not assume perfect corpus completeness unless a deterministic seed
  inventory or official bulk source has been reconciled.

## Product constraints

- The source of truth is the official NZ Legislation API and the repository
  metadata produced from it.
- External publishing steps depend on API credentials and should stay
  non-destructive by default.
- The pipeline must remain safe to rerun in CI and on a maintainer workstation.
