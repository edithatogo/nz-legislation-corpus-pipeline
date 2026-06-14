# Plan - Multi-Git and Multi-Archive Mirroring

## Phase 1: Git Remote Mirror Setup

- [x] Task: Write `.github/workflows/mirror_sync.yml` to support automated SSH mirroring to secondary Git remotes (GitLab/Codeberg).
- [x] Task: Add fail-closed local guardrails so the workflow skips when mirror secrets are absent and rejects non-SSH mirror URLs.
- [ ] Gated task: Configure repository secrets `GIT_MIRROR_URL` and `GIT_MIRROR_SSH_PRIVATE_KEY` on GitHub.
- [ ] Gated task: Verify successful manual and push triggers for mirror sync.

## Phase 2: Multi-Archive Integration & OSF Policy

- [x] Task: Create `docs/osf-optional-mirror-policy.md` matching sister `corpus-nz-hansard` repository.
- [x] Task: Validate the OSF policy using a Python validator script.
- [ ] Gated task: Conductor - User Manual Verification 'Phase 2: Multi-Archive Integration & OSF Policy' (Protocol in workflow.md).

## Local Evidence - 2026-06-14

- Chrome/browser-profile/account work: not approved for this lane, so no Chrome or browser-profile action was taken.
- Local mirror workflow review: `.github/workflows/mirror_sync.yml` now skips when `GIT_MIRROR_URL` or `GIT_MIRROR_SSH_PRIVATE_KEY` is absent and fails closed for non-SSH mirror URLs.
- OSF policy surface: `docs/osf-optional-mirror-policy.md` exists and keeps OSF inactive pending full bootstrap, full Hugging Face upload, OSF project creation, and a future Conductor implementation track.
- Validation commands passed:
  - `python scripts/check_osf_optional_policy.py`
  - `pytest -q tests/test_osf_optional.py`
  - `pytest -q -p no:cacheprovider tests/test_osf_optional.py`
  - `python -m ruff check scripts/check_osf_optional_policy.py tests/test_osf_optional.py src/nz_legislation_corpus/osf_optional.py`
  - `actionlint .github/workflows/mirror_sync.yml`
- `uv run ruff ...` was not usable in this Windows/OneDrive sandbox because uv cache initialization failed with access denied; direct `python -m ruff` passed.
