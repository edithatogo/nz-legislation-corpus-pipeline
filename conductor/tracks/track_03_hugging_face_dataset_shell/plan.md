# Plan - Hugging Face Dataset Shell

## Tasks
- [ ] Create or confirm the Hugging Face dataset repository named by `HF_REPO_ID`.
- [ ] Run `scripts/create_huggingface_dataset_repo.sh "$HF_REPO_ID"` or equivalent API setup.
- [ ] Confirm the remote layout is root-based, not nested under `data/`.
- [ ] Confirm `.gitattributes`, dataset card metadata, and lightweight root placeholders are correct.
- [ ] Remove any legacy `data/...` placeholders if present.
