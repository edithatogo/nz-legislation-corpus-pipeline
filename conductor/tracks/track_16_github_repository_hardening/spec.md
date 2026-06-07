# Spec - GitHub Repository Hardening

## Status
blocked

## Goal
make the GitHub repository safe to operate as the automation controller for the live Hugging Face corpus.

## Acceptance Criteria
- Default branch is protected.
- Tests are required for code changes.
- Secret scanning and dependency alerts are enabled or explicitly documented as unavailable.
- Repository remains code-only.

## Evidence to Record
- GitHub repository URL.
- Branch protection summary.
- Enabled security settings.
- First passing CI run URL.

## Current Evidence
- No Git remote is configured, so the final GitHub repository URL, branch protection summary, enabled security settings, and CI run URL cannot be recorded yet.
- Local hardening helper `scripts/configure_github_hardening.sh` now attempts repo defaults, Dependabot vulnerability alerts, secret scanning, push protection, Dependabot security updates, branch protection, and a required tests status check.
- Local repository remains code-only: generated corpus/archive/cache paths are ignored and no tracked files exist under `data/`, `dist/`, `archive/`, `.tmp/`, `.hf_cache/`, `.pytest-tmp/`, `test-tmp/`, or `.track15-smoke/`.
- Local public-repo support files and minimum workflow permissions were reviewed.
