import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file using PyMuPDF (fitz).

    Args:
        file_path (str): The file path to the PDF document.

    Returns:
        list: A list where each element represents the text of a page in the PDF.
    """
    extracted_text = []

    try:
        # Open the PDF file using PyMuPDF
        pdf_document = fitz.open(file_path)

        for page_number in range(len(pdf_document)):
            # Load each page
            page = pdf_document[page_number]
            
            # Extract text from the page
            page_text = page.get_text("text")  # Extract text in 'text' mode
            
            if page_text.strip():
                extracted_text.append(page_text.strip())  # Clean and store the text
            else:
                extracted_text.append("")  # Handle empty pages gracefully

        pdf_document.close()  # Ensure the document is closed after processing

    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        raise

    return extracted_text


def index_pdf_text(extracted_text, file_name):
    """
    Indexes extracted text from a PDF file by page.

    Args:
        extracted_text (list): List of strings where each string represents the text of a page.
        file_name (str): The name of the PDF file being indexed.

    Returns:
        dict: A dictionary where keys are page numbers, and values are the corresponding page text.
    """
    indexed_text = {}

    try:
        for page_number, page_text in enumerate(extracted_text, start=1):
            # Add page text to the index dictionary
            indexed_text[page_number] = page_text

        print(f"Successfully indexed {len(indexed_text)} pages for file: {file_name}")

    except Exception as e:
        print(f"Error indexing PDF text: {e}")
        raise

    return indexed_text