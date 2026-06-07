# Plan - GitHub Repository Hardening

## Tasks
- [ ] Create or confirm the final GitHub repository. Blocked: no Git remote is configured.
- [ ] Push the code-only repository without `data/`, `dist/`, cache directories, or generated corpus files. Blocked until the final GitHub repository exists.
- [ ] Enable branch protection on the default branch. Blocked until the final GitHub repository exists.
- [ ] Require the tests workflow before merge once CI is stable. Blocked until branch protection/rulesets can be applied on GitHub.
- [ ] Enable secret scanning and push protection where available. Blocked until GitHub repository settings are available.
- [ ] Enable Dependabot alerts and dependency update PRs. Dependency update PR configuration is present in `.github/dependabot.yml`; live alert enablement is scripted but blocked until GitHub repository settings are available.
- [x] Confirm `CODEOWNERS`, issue templates, pull request template, security policy, and contribution docs are present if the repo is public.
- [x] Confirm workflows have minimum permissions and do not expose secrets in logs.

## Implementation Notes
- Added branch protection, required status check, Dependabot vulnerability alert, secret scanning, push protection, and Dependabot security update API calls to `scripts/configure_github_hardening.sh`.
- Confirmed `.gitignore` excludes generated corpus/archive/cache paths including `data/`, `dist/`, `.hf_cache/`, and `.track15-smoke/`.
- Confirmed no tracked files currently exist under generated corpus/archive paths.
- Confirmed support files exist: `SECURITY.md`, `CONTRIBUTING.md`, `.github/CODEOWNERS`, `.github/pull_request_template.md`, issue templates, Dependabot config, CodeQL, Scorecard, tests, doctor, Hugging Face sync, and annual Zenodo workflows.
- Workflow secret references are passed through environment variables and are not echoed directly; summaries include generated state/manifests and archive checksums only.
