# Implementation status

Implemented in this starter repository:

- API-first NZ Legislation client with X-Api-Key auth, request pacing, low-quota backoff, retries, 429 handling, and conservative 403 burst-limit handling.
- Configurable discovery via search terms and/or seed work IDs.
- XML/HTML text extraction.
- Normalized record schema and validation report.
- Deterministic partitioned Parquet writer with PyArrow content-defined chunking and page-index options when supported.
- Stable content hashing in manifests. Generated timestamps and local state do not force uploads.
- Unchanged records are preserved byte-for-byte so scrape timestamps do not churn `records.jsonl` or Parquet.
- Hugging Face upload wrapper using `hf upload-large-folder` with fallback to `HfApi.upload_folder`.
- Hugging Face upload path uses `HF_XET_HIGH_PERFORMANCE=1`.
- Zenodo draft/new-version/archive upload client using bucket uploads where available.
- `nzlc coverage-report` for corpus coverage and risk indicators.
- Ephemeral NZ Legislation identifiers containing `~` are explicitly flagged.
- GitHub Actions for live sync, annual Zenodo archive, weekly doctor, tests, CodeQL, and OpenSSF Scorecard.
- Dependabot config.
- GitHub CLI bootstrap scripts for creating a fresh repository and configuring Actions secrets/variables.
- Manual first-sync guardrails for `max_works=5` and increased request spacing in the bootstrap docs and workflow dispatch input.
- Conductor tracks, contracts, red-team review, prioritized recommendations, setup docs, security policy, and maintenance runbook.

Validated in this environment:

- Python source compiled successfully.
- Workflow YAML parsed successfully.
- Unit tests passed: `6 passed` for the new rate-limit client coverage.
- Ruff passed on the edited files.
- Credential-free local smoke fixture passed through validation, manifest generation, coverage reporting, and archive creation.

Not run in this environment:

- Live NZ Legislation API calls, because they require your `NZ_LEGISLATION_API_KEY`.
- Hugging Face upload, because it requires your `HF_TOKEN` and `HF_REPO_ID`.
- Zenodo upload, because it requires your `ZENODO_TOKEN`.

Important packaging note:

- `uv.lock` is included. CI and local bootstrap commands should use frozen installs so dependency resolution remains reproducible.

First maintainer actions:

1. Run `./scripts/first_run_local.sh` locally.
2. Create the fresh GitHub repo with `scripts/bootstrap_github_repo.sh`.
3. Add or verify GitHub secrets and variables.
4. Run `tests.yml`.
5. Run `hf_sync.yml` with `max_works=5` first.
6. Run `annual_zenodo_archive.yml` against Zenodo sandbox before production.
