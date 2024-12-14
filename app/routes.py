from flask import Blueprint, request, jsonify, render_template
import os
from .utils import extract_text_from_pdf

# Blueprint for main app routes
main_bp = Blueprint("main", __name__)

# Route to render the main page
@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route to handle file uploads
@main_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    try:
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
    except Exception as e:
        return jsonify({"error": f"File upload failed: {str(e)}"}), 500

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