# v0.4 notes

## Added

- Hugging Face API initialisation script: `scripts/init_huggingface_dataset.py`.
- Safer wrapper script: `scripts/create_huggingface_dataset_repo.sh`.
- Example Hugging Face environment file: `examples/huggingface.env.example`.
- Hugging Face setup guide: `docs/HUGGINGFACE_SETUP.md`.
- Connector handoff guide: `docs/HUGGINGFACE_CONNECTOR_HANDOFF.md`.

## Purpose

This version makes the Hugging Face side as low-touch as the GitHub side. Once the maintainer provides `HF_TOKEN`, the dataset repository can be created, initialised, and left to the GitHub Actions workflow for future data uploads.

## Still intentionally not included

- Live corpus data.
- Real API tokens or repository secrets.
