# Maintenance automation

The pipeline is designed so the maintainer usually only reviews alerts and annual archive drafts.

## Automated maintenance already included

- Daily Hugging Face live sync.
- No-change upload skip through stable `content_sha256` manifests.
- Weekly Dependabot checks for GitHub Actions and Python dependencies.
- Fixture-based test workflow.
- Coverage-risk report after sync.
- Annual Zenodo archive workflow, draft-first by default.

## Recommended optional GitHub settings

Enable these after the repository exists:

1. Secret scanning and push protection.
2. Dependabot alerts.
3. Private vulnerability reporting if the repo is public.
4. Branch protection on `main` requiring the `Tests` workflow.
5. Required reviewer on the `zenodo-production` environment before production publication.

## Human review cadence

Monthly:

- Check the latest `Hugging Face live sync` summary.
- Review `coverage_report.json` on Hugging Face.
- Merge safe Dependabot updates after tests pass.

Quarterly:

- Run a larger `max_works` manual sync to check for discovery drift.
- Review NZ Legislation API documentation for endpoint or rate-limit changes.

Annually:

- Run the Zenodo sandbox archive.
- Verify checksums.
- Review licensing/citation text.
- Publish the production Zenodo snapshot.
- Record the DOI in `CITATION.cff` and the Hugging Face dataset card.
