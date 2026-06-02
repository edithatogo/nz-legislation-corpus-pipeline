# Plan - GitHub Repository Hardening

## Tasks
- [ ] Create or confirm the final GitHub repository.
- [ ] Push the code-only repository without `data/`, `dist/`, cache directories, or generated corpus files.
- [ ] Enable branch protection on the default branch.
- [ ] Require the tests workflow before merge once CI is stable.
- [ ] Enable secret scanning and push protection where available.
- [ ] Enable Dependabot alerts and dependency update PRs.
- [ ] Confirm `CODEOWNERS`, issue templates, pull request template, security policy, and contribution docs are present if the repo is public.
- [ ] Confirm workflows have minimum permissions and do not expose secrets in logs.
