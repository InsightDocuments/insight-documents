from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from app.pdf_processing import extract_text_from_pdf, index_pdf_text

app = Flask(__name__)

# Set the upload folder path
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    """
    Checks if the uploaded file has a valid extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handles PDF file uploads, extracts and indexes text, and returns a success response.
    """
    # Check if a file is part of the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # Check if a file was selected
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate the file extension
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        try:
            # Save the uploaded file
            file.save(file_path)

            # Extract text from the PDF
            extracted_text = extract_text_from_pdf(file_path)

            # Index the extracted text
            indexed_text = index_pdf_text(extracted_text, filename)

            # (Optional) Print indexed text for debugging
            print(indexed_text)

            # Return a success response
            return jsonify({
                'message': 'File uploaded and processed successfully',
                'file_name': filename,
                'total_pages': len(indexed_text)
            }), 200

        except Exception as e:
            return jsonify({'error': f'An error occurred while processing the file: {str(e)}'}), 500

    else:
        return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400
            
# Route to handle search queries
@main_bp.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    file_name = request.form.get("file_name")
    
    if not query or not file_name:
        return jsonify({"error": "Query and file name are required"}), 400

    file_path = os.path.join("uploads", file_name)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    try:
        # Extract text from the PDF file
        text = extract_text_from_pdf(file_path)
        
        # Mock response for now (to be replaced with real NLP processing)
        response = f"Mock response to '{query}': Relevant content here."
        
        return jsonify({"query": query, "response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500