# Plan - Maintenance Doctor And Alerting

## Tasks
- [x] Confirm `.github/workflows/doctor.yml` exists locally.
- [x] Confirm local non-network doctor runs without mutating corpus data.
- [ ] Confirm GitHub Actions notifications reach the maintainer.
- [x] Decide whether to add a lightweight webhook or issue creation on repeated failures.
- [x] Review Dependabot configuration and security workflows.

## Current blocker

- No Git remote is configured, so `.github/workflows/doctor.yml` cannot be confirmed enabled on the default branch.
- `GITHUB_REPOSITORY`, `GH_TOKEN`, `NZ_LEGISLATION_API_KEY`, `HF_TOKEN`, `HF_REPO_ID`, `ZENODO_TOKEN`, and `ARCHIVE_CREATORS_JSON` are not configured in the local environment.
- Live network doctor and notification delivery require a target GitHub repository plus Track 02 secrets/variables.
- Alerting decision: use GitHub Actions default notifications initially; defer webhook or issue creation until a live failure pattern justifies it.
