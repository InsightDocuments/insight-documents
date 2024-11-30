import os
import tempfile
import sys
import os
import pytest  # Ensure pytest is imported

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
@pytest.fixture
def client():
    """Set up a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = tempfile.mkdtemp()
    client = app.test_client()

    yield client

    # Clean up temporary upload folder
    for file in os.listdir(app.config['UPLOAD_FOLDER']):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))
    os.rmdir(app.config['UPLOAD_FOLDER'])

def test_upload_valid_file(client):
    """Test uploading a valid PDF file."""
    # Create a temporary file to mimic a PDF upload
    data = {
        'file': (tempfile.NamedTemporaryFile(suffix=".pdf"), "test.pdf")
    }
    # Post the file and follow the redirect
    response = client.post('/upload', data=data, content_type='multipart/form-data', follow_redirects=True)

    # Check the response
    assert response.status_code == 200  # Should render the homepage
    assert b"File uploaded successfully" in response.data  # Flash message should be present