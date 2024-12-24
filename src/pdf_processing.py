import pdfplumber
import sqlite3

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file, page by page.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        dict: Dictionary with page numbers as keys and text as values.
    """
    extracted_data = {}
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                extracted_data[page_number] = page.extract_text() or ""
    except Exception as e:
        print(f"Error processing file {pdf_path}: {e}")
    return extracted_data

def initialize_database(db_path="documents.db"):
    """
    Initializes the SQLite database and creates the 'documents' table if it does not exist.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            page_number INTEGER,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_to_database(data, title, db_path="documents.db"):
    """
    Saves extracted PDF data to the SQLite database.

    Args:
        data (dict): Extracted text data with page numbers as keys and text as values.
        title (str): Title of the document.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for page_number, text in data.items():
        cursor.execute('''
            INSERT INTO documents (title, page_number, content)
            VALUES (?, ?, ?)
        ''', (title, page_number, text))
    conn.commit()
    conn.close()