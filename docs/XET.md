# What Xet is and why this pipeline uses it

Xet is Hugging Face Hub's newer storage backend for large model and dataset files. Historically, Hub repositories used Git LFS pointers for large files. Xet keeps normal Hub repository workflows but stores large content in a content-addressed backend with chunk-level deduplication.

In practical terms for this corpus:

- If a Parquet file changes slightly, Xet can upload only new/changed chunks instead of treating the whole file as a totally new blob.
- This is especially useful for an evolving legal corpus where daily updates may affect a small number of instruments or versions.
- The pipeline therefore writes deterministic, optimized Parquet shards and uses `hf upload-large-folder`/`huggingface_hub` with `hf-xet` installed.
- Xet is not magic: if we rewrite files with unstable ordering or different Parquet options every run, deduplication gets worse. Stable ordering, stable partitioning, and consistent writer options are part of the contract.

Design implication: Hugging Face is the live operational hub; GitHub holds code only; Zenodo receives annual immutable archives.


For high-throughput uploads, set `HF_XET_HIGH_PERFORMANCE=1`. Do not use the deprecated `HF_HUB_ENABLE_HF_TRANSFER` flag.
