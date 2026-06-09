# Spec - Bleeding Edge Versioning And Release Automation

## Status
todo

## Goal

Implement SemVer/dataset/schema version governance, Release Please-style changelog automation, and consistency checks.

## Acceptance Criteria

- Aligns with `docs/bleeding-edge-versioning-ci-quality.md`.
- Preserves `corpus-nz-legislation` and `corpus-nz-hansard` naming.
- Uses Rust-backed tooling where practical: `uv`, `ruff`, `typos`, `zizmor`, `taplo`, and local `ripgrep` guidance.
- Keeps publication to Hugging Face and Zenodo behind validation gates.
- For Zenodo work, uses or formally evaluates `https://github.com/zenodraft/zenodraft`.
