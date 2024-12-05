import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_upload_file_no_file(self):
        response = self.client.post("/upload", data={})
        self.assertEqual(response.status_code, 400)

    def test_search_no_query(self):
        response = self.client.post("/search", data={})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()