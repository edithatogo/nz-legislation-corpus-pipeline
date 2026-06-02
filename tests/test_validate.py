from pathlib import Path

from nz_legislation_corpus.normalize import normalize_version_record
from nz_legislation_corpus.utils import write_jsonl
from nz_legislation_corpus.validate import validate_records


def test_validate_record(tmp_path: Path):
    xml = Path("tests/fixtures/sample_legislation.xml").read_bytes()
    record = normalize_version_record(
        {
            "title": "Sample Act 2026",
            "version_id": "sample-version",
            "work_id": "sample-work",
            "legislation_status": "current",
            "legislation_type": "act",
            "formats": [{"type": "xml", "url": "https://example.invalid/sample.xml"}],
        },
        raw_content=xml,
        raw_content_url="https://example.invalid/sample.xml",
        raw_content_type="application/xml",
    )
    path = tmp_path / "records.jsonl"
    write_jsonl(path, [record])
    report = validate_records(path, schema_path=Path("schemas/legislation_record.schema.json"))
    assert report["ok"]



def test_ephemeral_identifier_flagged():
    from nz_legislation_corpus.normalize import normalize_version_record

    record = normalize_version_record({"version_id": "secondary-legislation_pco-drafted_~2026_1_en_~2026-01-01", "work_id": "secondary-legislation_pco-drafted_~2026_1", "title": "T"})
    assert record["id_is_ephemeral"] is True
    assert "~" in record["id_ephemeral_reason"]
