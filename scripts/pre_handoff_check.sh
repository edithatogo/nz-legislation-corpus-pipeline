#!/usr/bin/env bash
set -euo pipefail

bad=0

fail() {
  echo "ERROR: $*" >&2
  bad=1
}

warn() {
  echo "WARN: $*" >&2
}

if find . -type d -name __pycache__ | grep -q .; then
  fail "__pycache__ directories are present. Remove them before handoff."
fi

if find . -type f -name '*.pyc' | grep -q .; then
  fail "compiled Python files are present. Remove *.pyc before handoff."
fi

for path in data dist .venv .hf_cache .pytest_cache .ruff_cache .mypy_cache; do
  if [ -e "$path" ]; then
    fail "$path exists and should not be committed."
  fi
done

if [ ! -f pyproject.toml ]; then
  fail "pyproject.toml missing."
fi

if ! grep -q 'version = "0.5.0"' pyproject.toml; then
  warn "pyproject version is not 0.5.0; confirm this is intentional."
fi

if [ ! -f uv.lock ]; then
  warn "uv.lock is not present. Generate locally with: uv lock"
fi

if grep -R "data/parquet" -n README.md DATASET_CARD.md docs scripts 2>/dev/null | grep -v PRE_HANDOFF_RECOMMENDATIONS.md | grep -v pre_handoff_check.sh; then
  warn "Found data/parquet references. Confirm whether they should be root-based parquet/ references."
fi

if git status --short >/dev/null 2>&1; then
  echo "Git working tree status:"
  git status --short || true
fi

if [ "$bad" -ne 0 ]; then
  exit 1
fi

echo "Pre-handoff check completed. Review warnings before bootstrap."
