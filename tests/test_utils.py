import unittest
import os
from app.utils import extract_text_from_pdf

class TestUtils(unittest.TestCase):
    def test_extract_text_from_pdf(self):
        # Create a temporary PDF file for testing
        test_pdf_path = "test.pdf"
        with open(test_pdf_path, "wb") as f:
            f.write(b"%PDF-1.4\n1 0 obj\n<<>>\nendobj\ntrailer\n<<>>\nstartxref\n0\n%%EOF")

        with self.assertRaises(Exception):
            extract_text_from_pdf(test_pdf_path)

        os.remove(test_pdf_path)

if __name__ == "__main__":
    unittest.main()