#!/usr/bin/env bash
set -euo pipefail

HF_REPO_ID="${1:-${HF_REPO_ID:-}}"
if [[ -z "$HF_REPO_ID" ]]; then
  echo "Usage: HF_TOKEN=... scripts/create_huggingface_dataset_repo.sh <namespace/dataset-name>" >&2
  exit 2
fi
if [[ -z "${HF_TOKEN:-}" ]]; then
  echo "HF_TOKEN is required." >&2
  exit 2
fi

if ! python - <<'PY' >/dev/null 2>&1
import huggingface_hub
PY
then
  python -m pip install -U "huggingface_hub[hf_xet]" >/dev/null
fi

HF_REPO_ID="$HF_REPO_ID" python scripts/init_huggingface_dataset.py
