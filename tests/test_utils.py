import os
import pytest
from app.utils import extract_text_from_pdf

@pytest.fixture
def pdf_file(tmp_path):
    file_path = tmp_path / "test.pdf"
    with open(file_path, "wb") as f:
        f.write(b"%PDF-1.4 Dummy PDF Content")
    return str(file_path)

def test_extract_text_from_pdf_success(pdf_file):
    text = extract_text_from_pdf(pdf_file)
    assert text == "Dummy PDF Content"  # Adjust the assertion based on actual text extraction.

def test_extract_text_from_pdf_invalid_path():
    invalid_path = "nonexistent.pdf"
    with pytest.raises(RuntimeError) as excinfo:
        extract_text_from_pdf(invalid_path)
    assert "Error extracting text from PDF" in str(excinfo.value)