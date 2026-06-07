# Plan - Downstream Researcher Usability

## Tasks
- [ ] Add a small public sample split if useful for users who do not want the full corpus.
- [x] Add DuckDB or Polars examples that query Parquet directly from Hugging Face.
- [x] Add a minimal data dictionary from schema fields.
- [x] Decide whether to add a Hugging Face Space for browsing/search after core maintenance is stable.

## Current blocker

- `docs/researcher_quickstart.md` and `docs/data_dictionary.md` are added.
- Public sample split is deferred until the live Hugging Face dataset exists.
- Hugging Face Space is deferred until the dataset pipeline and live hub are stable.
- Example command output and sample dataset revision cannot be recorded until Tracks 03 and 08 publish the dataset.
