# Draft public launch release note

Status: draft only. Do not publish until `docs/public_launch_decision.md` is changed to a launch decision with live evidence.

## New Zealand Legislation Corpus

The New Zealand Legislation Corpus is an API-first pipeline and dataset for machine-readable New Zealand legislation records. It publishes normalized records, source provenance, optimized Parquet files, validation reports, coverage metrics, and manifest hashes for reproducible research use.

## Coverage

Coverage status at launch: to be filled from the final launch checklist.

Do not claim full New Zealand legislation coverage unless Track 04 has proven the discovery method against an authoritative inventory. If Track 04 is not proven, state the dataset is partial or API-discovery based and include the configured discovery boundary.

Fields to fill:

```text
Record count:
Legislation types included:
Statuses included:
Discovery method:
Known gaps:
Manifest hash:
Hugging Face revision:
```

## Caveats

- This dataset is not legal advice.
- Text extraction is conservative and may not preserve every legal structure.
- Coverage is limited to the verified discovery scope.
- Incorporated-by-reference material, third-party material, agency website text, logos, emblems, and non-legislative linked content may have separate rights or restrictions.
- Users should cite the manifest hash for live/current use.

## Update cadence

The intended operating model is:

- daily or regular Hugging Face sync after the first verified upload;
- weekly non-destructive service doctor checks;
- monthly coverage/reconciliation review;
- annual Zenodo archive workflow, sandbox first and production only after approval.

## Citation

For live/current use, cite:

```text
New Zealand Legislation Corpus, Hugging Face dataset URL, access date, and manifest hash.
```

For fixed-version academic citation, cite the annual Zenodo DOI snapshot once available.

## Archive plan

The live dataset is maintained on Hugging Face. Annual immutable snapshots are intended for Zenodo DOI-backed archival release after sandbox verification and production approval.
