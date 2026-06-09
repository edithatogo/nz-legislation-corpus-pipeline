.PHONY: install test smoke validate manifest archive

install:
	uv sync --all-extras

test:
	uv run pytest -q

smoke:
	ARCHIVE_CREATORS_JSON='[{"name":"Test Maintainer"}]' NZLC_OUTPUT_DIR=data uv run nzlc smoke-fixture --output-dir data

validate:
	NZLC_OUTPUT_DIR=data uv run nzlc validate

manifest:
	NZLC_OUTPUT_DIR=data uv run nzlc manifest

archive:
	NZLC_OUTPUT_DIR=data uv run nzlc archive --year $${YEAR:-2026} --output-dir dist/archive

bootstrap-github:
	./scripts/bootstrap_github.sh

first-run:
	./scripts/first_run_local.sh

security-note:
	@echo "Configure GitHub environment required reviewers for zenodo-production before production publish."

.PHONY: quality format-check type-check

quality:
	uv run ruff check src/nz_legislation_corpus tests
	uv run ruff format --check src/nz_legislation_corpus tests
	uv run mypy src/nz_legislation_corpus
	uv run pytest -q

format-check:
	uv run ruff format --check src/nz_legislation_corpus tests

type-check:
	uv run mypy src/nz_legislation_corpus

