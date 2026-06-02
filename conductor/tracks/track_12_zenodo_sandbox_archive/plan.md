# Plan - Zenodo Sandbox Archive

## Tasks
- [ ] Set Zenodo sandbox token and sandbox API URL.
- [ ] Run `uv run nzlc archive --year <year> --output-dir dist/archive`.
- [ ] Run `uv run nzlc zenodo-upload --year <year> --archive-dir dist/archive` against sandbox.
- [ ] Verify archive manifest and checksums.
- [ ] Verify duplicate-file replacement behavior if rerun.
