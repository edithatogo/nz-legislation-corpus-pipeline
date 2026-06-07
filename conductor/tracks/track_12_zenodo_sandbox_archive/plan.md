# Plan - Zenodo Sandbox Archive

## Tasks
- [ ] Set Zenodo sandbox token and sandbox API URL.
- [ ] Run `uv run nzlc archive --year <year> --output-dir dist/archive`.
- [ ] Run `uv run nzlc zenodo-upload --year <year> --archive-dir dist/archive` against sandbox.
- [ ] Verify archive manifest and checksums.
- [ ] Verify duplicate-file replacement behavior if rerun.

## Current blocker

- `ZENODO_TOKEN` is not configured in the local environment.
- `ARCHIVE_CREATORS_JSON` is not configured in the local environment.
- `data/` is absent, so there is no corpus to archive.
- `dist/archive` is absent, so there are no archive files to upload or verify.
- The duplicate-file replacement path exists in code, but it cannot be proven without a sandbox draft and token.
