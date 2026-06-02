# Pre-handoff recommendations

These are the last checks before a local coding agent takes over.

## Must fix before bootstrap

- Keep the repository code-only; never push generated corpus files to GitHub.
- Commit a local `uv.lock` and use frozen CI installs after it exists.
- Keep the Hugging Face remote layout root-based: `parquet/`, `raw_xml/`, `manifests/`, `_state/`.
- Treat source discovery as an explicit coverage problem. Search terms are not a proof of completeness.
- Use environment-protected Zenodo publication. Draft creation may be unattended; production publication should require approval.

## Should fix in first local-agent sprint

- Mocked API tests for pagination and rate-limit responses are now in place for the NZ API client.
- Keep the first-sync throttle plan in the bootstrap docs and workflow dispatch input.
- Replace any broad default search term assumptions with a seed-list or official bulk/source enumeration strategy.
- Make the dataset card distinguish clearly between code license, legislation copyright status, and incorporated-by-reference caveats.
- Add a local smoke report artifact after first run.

## Do not block handover on these

- Hugging Face DOI generation.
- SLSA/provenance attestation.
- OSF mirror.
- Full action SHA pinning.
