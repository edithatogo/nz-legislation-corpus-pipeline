---
license: other
language:
- en
tags:
- new-zealand
- legislation
- law
- legal-corpus
- parquet
- xet
pretty_name: New Zealand Legislation Corpus
---

# New Zealand Legislation Corpus

## Summary

This dataset contains machine-readable New Zealand legislation records collected through the official New Zealand Legislation API and published as optimized Parquet shards for live use.

## Source provenance

Records include source URLs, API URLs, format URLs, hashes, scrape timestamps, and pipeline version metadata.

## Data fields

Core fields include:

- `stable_id`
- `work_id`
- `version_id`
- `title`
- `legislation_type`
- `legislation_status`
- `source_url`
- `api_url`
- `xml_url`
- `html_url`
- `pdf_url`
- `text`
- `text_sha256`
- `source_hash`

## Intended use

- legal information retrieval
- statutory text search
- legal NLP experiments
- reproducible public-law data analysis
- annual comparison of statutory change

## Limitations

- Corpus completeness depends on the configured discovery strategy.
- Text extraction is intentionally conservative and may not preserve all legal structure.
- Incorporated-by-reference material may not be included or may have different rights.
- This dataset is not legal advice.

## Loading examples

```python
from datasets import load_dataset

ds = load_dataset("your-name/nz-legislation-corpus", split="train", streaming=True)
for row in ds.take(1):
    print(row["title"])
```

```python
import pyarrow.dataset as ds

dataset = ds.dataset("data/parquet", format="parquet", partitioning="hive")
table = dataset.to_table(columns=["title", "legislation_type", "text"])
```

```sql
-- DuckDB example
SELECT title, legislation_type
FROM read_parquet('hf://datasets/your-name/nz-legislation-corpus/parquet/**/*.parquet')
LIMIT 10;
```

## Update cadence

The live Hugging Face dataset is intended for daily or regular updates. DOI-backed snapshots are intended for annual Zenodo archival releases.

## Citation

Use the annual Zenodo DOI for academic citation once available. For live use, cite the Hugging Face repository and the manifest hash.

## Legal caveat

Check the New Zealand Legislation copyright page and your own institution's policies before redistributing or relying on the dataset. This dataset is provided for information and research support, not legal advice.
