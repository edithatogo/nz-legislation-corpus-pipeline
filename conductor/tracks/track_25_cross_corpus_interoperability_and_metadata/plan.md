# Plan - Cross Corpus Interoperability And Metadata

## Phase 1 - Cross-corpus roadmap mapping

- [ ] Review `corpus-nz-hansard` tracks for search/RAG, RDF, Akoma Ntoso, and metadata endpoints.
- [ ] Map which patterns apply to legislation and which are Hansard-specific.
- [ ] Document optional artifact governance in legislation docs.

## Phase 2 - Researcher artifacts

- [ ] Add or refine DuckDB/Polars examples for Hugging Face Parquet access.
- [ ] Define optional search/RAG index contract with citation/provenance requirements.
- [ ] Define validation manifest requirements for derived indexes.

## Phase 3 - Interoperability metadata

- [ ] Define Croissant metadata scope for ML-ready discovery.
- [ ] Define RO-Crate and Frictionless descriptors for research-object packaging.
- [ ] Define DCAT/PROV-O metadata surface and stable URI policy.
- [ ] Evaluate Akoma Ntoso export as a generated endpoint, not the internal schema.

## Phase 4 - Publication environments

- [ ] Decide whether derived artifacts publish to Hugging Face, Zenodo, OSF, GitHub release assets, or all/none.
- [ ] Require each environment to declare access policy, file layout, checksums, and citation guidance.
- [ ] Cross-link equivalent Hansard derived artifacts where useful.

## Verification

- [ ] Roadmap docs mention the optional endpoint families.
- [ ] No base dependency expansion occurs without a separate implementation track.
- [ ] Conductor tracks.md registers this track.
