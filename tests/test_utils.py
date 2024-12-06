import os
import pytest
from app.utils import extract_text_from_pdf

def test_extract_text_from_pdf():
    # Path to a sample PDF file
    file_path = os.path.join("uploads", "Govt-job.pdf")

    # Ensure the file exists
    assert os.path.exists(file_path), "PDF file does not exist in the uploads directory"

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # Assert the extracted text is not empty
    assert extracted_text.strip() != "", "Extracted text is empty"

    # (Optional) Print the extracted text for debugging
    print(extracted_text)