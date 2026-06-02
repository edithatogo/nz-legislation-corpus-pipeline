# Tech Stack

## Runtime

- Python 3.11+
- Packaging with `hatchling`
- CLI entry point: `nzlc`

## Core libraries

- `typer` for the command-line interface.
- `requests` for API access.
- `rich` for terminal output.
- `pyarrow` for Parquet writing and data handling.
- `defusedxml` for safe XML parsing.
- `huggingface_hub` and `hf-xet` for Hugging Face dataset publishing.
- `jsonschema` for schema validation.
- `zstandard` for compression support.

## Development tools

- `pytest` for tests.
- `ruff` for linting and import sorting.
- `mypy` for static typing.
- `pre-commit` for local checks.

## Data and artifact formats

- JSONL for normalized records and provenance-oriented outputs.
- XML and HTML as source/provenance formats.
- Parquet for optimized tabular dataset shards.
- JSON manifests and checksum files for validation and audit trails.

## External services

- Official New Zealand Legislation API.
- Hugging Face Datasets.
- Zenodo.
- GitHub Actions for CI and release automation.

## Project structure

- `src/nz_legislation_corpus/` contains the application code.
- `tests/` contains unit and integration-style tests.
- `docs/` contains operational and release documentation.
- `schemas/` contains validation schemas and related artifacts.
- `scripts/` contains local and release automation helpers.

## Implementation notes

- Favor deterministic outputs and stable ordering where possible.
- Keep external-service interactions isolated behind narrow interfaces.
- Preserve provenance and hashes so downstream artifacts remain auditable.
