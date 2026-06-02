# Devil's advocate and red-team review

## 1. Discovery risk: the official API may not expose a perfect "all changed since X" feed

The New Zealand Legislation API is search- and version-oriented. If there is no first-class complete enumeration or modified-since endpoint, a fully automatic daily corpus can miss records unless we maintain deterministic seed work IDs or obtain an official export.

Mitigation implemented:

- `nzlc sync` accepts seed work IDs.
- Search terms are configurable instead of hardcoded.
- The sync state records known version hashes.
- The docs recommend an initial bootstrap from a seed file or official bulk source where possible.

Priority: P0. Solve before claiming corpus completeness.

## 2. Legal/source-of-truth risk

The public site states there is no copyright in New Zealand legislation, but incorporated-by-reference material may still be copyrighted. Metadata, website text, agency pages, and non-legislative content may have different rules.

Mitigation implemented:

- Dataset card has legal caveats.
- Records keep source URL, API URL, XML URL, and hashes for provenance.
- Raw XML storage is optional but recommended for auditability.

Priority: P0.

## 3. Zenodo large-file API risk

Zenodo's older deposition file endpoint and newer bucket file API have different limits and behaviours. A 6GB annual archive should use the bucket URL, but sandbox testing is mandatory.

Mitigation implemented:

- Zenodo upload defaults to sandbox in workflow.
- Publish is opt-in.
- The client refuses to proceed without a bucket URL for large-file upload.
- The workflow uses a protected production environment named `zenodo-production`; draft/sandbox runs use `zenodo-sandbox`.

Priority: P0.

## 4. Xet/Parquet deduplication can be defeated

If row ordering, shard boundaries, compression settings, or Parquet writer options change frequently, Xet will still work but efficiency suffers.

Mitigation implemented:

- Stable ordering by `stable_id`.
- Stable partitions by legislation type and year.
- Consistent Parquet writer options.
- Content-defined chunking and page index are enabled when PyArrow supports them.

Priority: P1.

## 5. GitHub Actions runtime and rate limits

A first bootstrap of a 6GB corpus may exceed default workflow time or hit NZ API quotas.

Mitigation implemented:

- Configurable request pacing.
- Conservative 403/429 handling.
- `max_works` smoke-test limit.
- Seed work IDs to support segmented bootstraps.

Priority: P1.

## 6. Maintainer burden

Long-term risk is not code difficulty; it is secret expiry, schema drift, API endpoint changes, and unnoticed failed schedules.

Mitigation implemented:

- `nzlc doctor` command.
- GitHub step summaries.
- Fixture smoke tests.
- Dependabot configuration.
- Explicit contracts and conductor tracks.

Priority: P1.
