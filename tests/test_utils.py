import pytest
from app.utils import extract_text_from_pdf

@pytest.fixture
def pdf_file(tmp_path):
    file_path = tmp_path / "test.pdf"
    # Create a valid PDF file
    with open(file_path, "wb") as f:
        f.write(
            b"%PDF-1.4\n"
            b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n"
            b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n"
            b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] >>\nendobj\n"
            b"xref\n0 4\n0000000000 65535 f \n0000000010 00000 n \n0000000060 00000 n \n0000000110 00000 n \n"
            b"trailer\n<< /Root 1 0 R /Size 4 >>\nstartxref\n170\n%%EOF"
        )
    return str(file_path)

def test_extract_text_from_pdf_success(pdf_file):
    text = extract_text_from_pdf(pdf_file)
    assert isinstance(text, str)
    # Add more assertions based on the expected content of the PDF