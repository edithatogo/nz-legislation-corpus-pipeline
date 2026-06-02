# v0.5 notes

Pre-handover hardening after the v0.4 review.

Changes:

- Fixed the annual Zenodo workflow environment expression so scheduled annual runs use the production environment for production drafts, while manual sandbox runs stay in the sandbox environment.
- Aligned package versions: `pyproject.toml` and `src/nz_legislation_corpus/__init__.py` now report `0.5.0`.
- Removed duplicate Hugging Face sync imports from the CLI.
- Switched Dependabot's Python ecosystem from `pip` to `uv` and added pre-commit updates.
- Corrected Hugging Face bootstrap layout: remote corpus files live at repository root, not under an extra `data/` prefix.
- Added cleanup for legacy `data/...` Hugging Face placeholders.
- Added `docs/LOCAL_AGENT_HANDOVER.md`.
- Removed Python bytecode/cache files from the package.

Recommended next step: run the offline smoke test before creating the live repositories.
