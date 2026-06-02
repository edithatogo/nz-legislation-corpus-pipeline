#!/usr/bin/env bash
set -euo pipefail

REPO_FULL_NAME="${1:-${GITHUB_REPOSITORY:-edithatogo/nz-legislation-corpus-pipeline}}"

gh api --method PATCH "repos/$REPO_FULL_NAME" \
  -f has_wiki=false \
  -f delete_branch_on_merge=true \
  -f allow_squash_merge=true \
  -f allow_merge_commit=false \
  -f allow_rebase_merge=true >/dev/null

gh api --method PUT "repos/$REPO_FULL_NAME/environments/zenodo-sandbox" >/dev/null || true
gh api --method PUT "repos/$REPO_FULL_NAME/environments/zenodo-production" >/dev/null || true

cat <<EOF
Configured base hardening for $REPO_FULL_NAME.

Manual follow-up:
- Settings → Environments → zenodo-production → add required reviewers.
- Settings → Rulesets/Branches → require the tests workflow before merging.
EOF
