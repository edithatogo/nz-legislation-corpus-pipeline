from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any

from huggingface_hub import HfApi, hf_hub_download
from huggingface_hub.utils import EntryNotFoundError, RepositoryNotFoundError

from .utils import read_json

DEFAULT_EXCLUDES = [
    ".git/**",
    "**/.DS_Store",
    "**/__pycache__/**",
    "**/*.pyc",
    ".pytest_cache/**",
    ".ruff_cache/**",
    "cache/huggingface/**",
    ".cache/**",
]


def remote_manifest(repo_id: str, *, token: str | None = None, revision: str = "main") -> dict[str, Any] | None:
    try:
        path = hf_hub_download(
            repo_id=repo_id,
            filename="manifests/latest_manifest.json",
            repo_type="dataset",
            token=token,
            revision=revision,
        )
        return read_json(Path(path), default=None)
    except (EntryNotFoundError, RepositoryNotFoundError, FileNotFoundError):
        return None


def create_dataset_repo_if_needed(repo_id: str, *, token: str | None = None, private: bool = False) -> None:
    api = HfApi(token=token)
    api.create_repo(repo_id=repo_id, repo_type="dataset", private=private, exist_ok=True)


def upload_large_folder(
    repo_id: str,
    folder: Path,
    *,
    token: str | None = None,
    revision: str = "main",
    quiet: bool = True,
    num_workers: int | None = None,
) -> str:
    """Upload with `hf upload-large-folder`, falling back to HfApi.upload_folder.

    `hf_xet` is enabled by default in modern huggingface_hub. HF_XET_HIGH_PERFORMANCE=1
    requests the high-throughput path without the deprecated hf_transfer flag.
    """
    env = os.environ.copy()
    if token:
        env["HF_TOKEN"] = token
    env.setdefault("HF_XET_HIGH_PERFORMANCE", "1")

    cmd = [
        "hf",
        "upload-large-folder",
        repo_id,
        str(folder),
        "--repo-type",
        "dataset",
        "--revision",
        revision,
    ]
    if quiet:
        cmd.extend(["--format", "quiet"])
    if num_workers:
        cmd.extend(["--num-workers", str(num_workers)])
    for pattern in DEFAULT_EXCLUDES:
        cmd.extend(["--exclude", pattern])
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True, env=env)
        return result.stdout.strip() or result.stderr.strip() or f"https://huggingface.co/datasets/{repo_id}/tree/{revision}"
    except (FileNotFoundError, subprocess.CalledProcessError):
        api = HfApi(token=token)
        api.upload_folder(
            repo_id=repo_id,
            repo_type="dataset",
            folder_path=str(folder),
            path_in_repo=".",
            revision=revision,
            commit_message="Sync NZ legislation corpus",
            ignore_patterns=DEFAULT_EXCLUDES,
        )
        return f"https://huggingface.co/datasets/{repo_id}/tree/{revision}"
