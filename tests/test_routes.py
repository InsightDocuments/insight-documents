import pytest
import io
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_upload_success(client):
    data = {
        'file': (io.BytesIO(b"%PDF-1.4 Dummy PDF Content"), 'test.pdf')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert response.get_json()['message'] == 'File uploaded successfully'

def test_upload_no_file(client):
    response = client.post('/upload', data={}, content_type='multipart/form-data')
    assert response.status_code == 400
    assert response.get_json()['error'] == 'No file part in the request'

def test_upload_invalid_extension(client):
    data = {
        'file': (io.BytesIO(b"Dummy text content"), 'test.txt')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Only PDF files are allowed'

def test_upload_empty_filename(client):
    data = {
        'file': (io.BytesIO(b"%PDF-1.4 Dummy PDF Content"), '')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert response.get_json()['error'] == 'No file selected'