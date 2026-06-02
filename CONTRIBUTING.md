# Contributing

## Local setup

```bash
uv sync --all-extras
./scripts/first_run_local.sh
```

## Development rules

- Do not commit generated corpus data.
- Keep schema changes explicit and documented.
- Add tests for validation, manifest, and normalization behavior.
- Keep workflows idempotent and safe to rerun.
- Keep Zenodo publication opt-in.

## Before opening a PR

```bash
uv run ruff check .
uv run pytest -q
ARCHIVE_CREATORS_JSON='[{"name":"Local Test"}]' uv run nzlc smoke-fixture --output-dir data
NZLC_OUTPUT_DIR=data uv run nzlc validate
NZLC_OUTPUT_DIR=data uv run nzlc manifest
```
