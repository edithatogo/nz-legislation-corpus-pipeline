# Low-maintenance improvement backlog

The current architecture is intentionally conservative. These improvements are prioritized for maximum robustness with minimum recurring maintenance.

## P0 — Do now

1. Use a fresh GitHub repository and keep corpus data out of GitHub.
2. Set GitHub Actions secrets and variables once through the bootstrap script.
3. Create the Hugging Face dataset repo before the first live sync.
4. Keep Zenodo publication opt-in and protected by a GitHub Environment.
5. Verify coverage with a seed work-ID list or official bulk inventory before claiming completeness.

## P1 — High value after first live run

1. Add a curated `seeds/work_ids.txt` from an official or manually verified inventory.
2. Add a coverage baseline JSON once you know expected counts by legislation type/status/year.
3. Add a monthly reconciliation workflow that compares API discovery against the seed inventory.
4. Publish a small public sample split for users who want to test loaders without downloading the full corpus.
5. Add a status badge and link the Hugging Face dataset card to the latest annual Zenodo DOI.

## P2 — Optional hardening

1. Add pre-commit hooks for Ruff, JSON schema validation, and secret scanning.
2. Add OpenSSF Scorecard or similar supply-chain checks if the repository becomes high-profile.
3. Add an issue-creation workflow on repeated sync failures, but avoid noisy alerting until the pipeline is stable.
4. Split annual archives for OSF only if you decide OSF should be a secondary mirror.

## Non-goals

- Do not push the corpus into GitHub.
- Do not make Zenodo the daily update target.
- Do not rewrite all Parquet files when only a few records changed.
- Do not claim complete corpus coverage from broad text search alone.
