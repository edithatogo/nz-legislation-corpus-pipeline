from pathlib import Path

from nz_legislation_corpus.extract_text import extract_text_from_html, extract_text_from_xml


def test_extract_text_from_xml():
    text = extract_text_from_xml(Path("tests/fixtures/sample_legislation.xml").read_bytes())
    assert "Sample Act 2026" in text
    assert "pipeline testing" in text


def test_extract_text_from_html():
    text = extract_text_from_html(Path("tests/fixtures/sample_legislation.html").read_bytes())
    assert "Sample Regulation 2026" in text
    assert "data-quality governance tests" in text
    assert "window.testOnly" not in text
