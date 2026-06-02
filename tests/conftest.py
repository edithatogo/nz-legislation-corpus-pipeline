from __future__ import annotations

import uuid
from pathlib import Path

import pytest


@pytest.fixture
def tmp_path() -> Path:
    """Provide a repo-local temporary directory for filesystem tests."""
    root = Path.cwd() / "test-tmp"
    root.mkdir(parents=True, exist_ok=True)
    path = root / f"case-{uuid.uuid4().hex}"
    path.mkdir()
    return path
