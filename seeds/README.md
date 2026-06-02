# Seed work IDs

Use this directory for deterministic corpus bootstrapping. Search-based discovery is useful but should not be treated as proof of full coverage. A curated work-ID seed list lets the pipeline re-fetch versions deterministically.

Run with:

```bash
uv run nzlc sync --seed-work-ids seeds/work_ids.txt
```

Keep large generated seed lists out of GitHub if they become bulky; store them on Hugging Face under `manifests/` or as an archive asset.
