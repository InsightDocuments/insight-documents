from src.pdf_processing import extract_text_from_pdf, save_to_database, initialize_database

# Initialize the database
initialize_database()

# Path to a sample PDF (replace with your actual file path)
pdf_path = "sample.pdf"
document_title = "Sample Document"

# Step 1: Extract text from the PDF
parsed_data = extract_text_from_pdf(pdf_path)
if not parsed_data:
    print("No data extracted. Please check the PDF file.")
else:
    print("Text extraction successful!")

# Step 2: Save the extracted data to the database
save_to_database(parsed_data, document_title)
print(f"Data from '{document_title}' has been saved to the database successfully!")