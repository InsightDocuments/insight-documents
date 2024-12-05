from flask import Blueprint, request, jsonify, render_template
import os
from .utils import extract_text_from_pdf

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    if file:
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200

@main_bp.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    file_name = request.form.get("file_name")

    if not query or not file_name:
        return jsonify({"error": "Query and file name are required"}), 400

    file_path = os.path.join("uploads", file_name)
    try:
        text = extract_text_from_pdf(file_path)
        # Mock a concise response for simplicity
        response = f"Mock response to '{query}': Relevant content here."
        return jsonify({"query": query, "response": response}), 200
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500