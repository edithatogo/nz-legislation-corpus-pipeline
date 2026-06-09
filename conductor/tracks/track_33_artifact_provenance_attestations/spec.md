# Spec - Artifact Provenance And Attestations

## Status
todo

## Goal

Add release evidence ledgers, GitHub artifact attestations or SLSA-style provenance, and signed/checksummed artifact policy.

## Acceptance Criteria

- Aligns with docs/bleeding-edge-versioning-ci-quality.md.
- Preserves corpus-nz-legislation and corpus-nz-hansard naming.
- Uses Rust-backed tooling where practical: uv, uff, 	ypos, zizmor, 	aplo, and local ipgrep guidance.
- Keeps publication to Hugging Face and Zenodo behind validation gates.
- For Zenodo work, uses or formally evaluates https://github.com/zenodraft/zenodraft.
