# Conductor tracks

These tracks are meant for either humans or coding agents. Each track has clear inputs, outputs, and stop conditions.

## Track A — Source discovery and intake

Owner: `NZLegislationClient` and `nzlc sync`.

Inputs:

- `NZ_LEGISLATION_API_KEY`
- `NZLC_SEARCH_TERMS` or `--seed-work-ids`
- API base URL

Outputs:

- raw XML/HTML under `data/raw_xml/`
- normalized records under `data/records.jsonl`
- sync state under `data/_state/sync_state.json`

Stop condition:

- all discovered versions attempted
- failed versions recorded in sync-state warnings

## Track B — Normalization and contracts

Owner: `normalize.py`, `extract_text.py`, schema.

Inputs:

- version metadata
- XML/HTML bytes

Outputs:

- records satisfying `schemas/legislation_record.schema.json`

Stop condition:

- `nzlc validate` passes

## Track C — Optimized Parquet / Xet efficiency

Owner: `parquet_writer.py`.

Inputs:

- normalized records

Outputs:

- partitioned Parquet under `data/parquet/`

Contracts:

- stable row order
- stable partition names
- consistent compression/options
- enable CDC and page index where supported

Stop condition:

- Parquet files written and readable by PyArrow

## Track D — Manifest and provenance

Owner: `manifest.py`.

Inputs:

- output data tree

Outputs:

- `data/manifests/latest_manifest.json`
- `data/manifests/latest_changes.json`

Stop condition:

- manifest hash generated and change report created

## Track E — Live Hugging Face publication

Owner: `hf_sync.py`, `hf_sync.yml`.

Inputs:

- data tree
- `HF_TOKEN`
- `HF_REPO_ID`

Outputs:

- Hugging Face dataset repository update

Stop condition:

- upload completed or skipped because remote manifest matches

## Track F — Annual archival DOI

Owner: `archive.py`, `zenodo.py`, `annual_zenodo_archive.yml`.

Inputs:

- current Hugging Face corpus state
- Zenodo token
- archive metadata variables

Outputs:

- `.tar.zst` or `.tar.gz` archive
- manifest
- checksum file
- Zenodo draft or published DOI-backed record

Stop condition:

- draft URL created; publication only after explicit approval

## Track G — Maintenance automation

Owner: `tests.yml`, Dependabot, doctor command.

Inputs:

- source code changes
- dependency updates

Outputs:

- CI results
- fixture smoke corpus
- failure summaries

Stop condition:

- tests pass and no destructive operations were performed
