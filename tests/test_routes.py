import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_upload_success(client):
    file_data = b"%PDF-1.4 Dummy PDF Content"
    data = {"file": (file_data, "test.pdf")}
    response = client.post("/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["message"] == "File uploaded successfully"

def test_upload_no_file(client):
    response = client.post("/upload", data={}, content_type="multipart/form-data")
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["error"] == "No file part in the request"

def test_upload_invalid_extension(client):
    file_data = b"Dummy text content"
    data = {"file": (file_data, "test.txt")}
    response = client.post("/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["error"] == "Only PDF files are allowed"

def test_upload_empty_filename(client):
    file_data = b"%PDF-1.4 Dummy PDF Content"
    data = {"file": (file_data, "")}
    response = client.post("/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data["error"] == "No file selected"