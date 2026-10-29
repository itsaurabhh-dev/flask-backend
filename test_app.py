import unittest
from app import app

class T(unittest.TestCase):
    def test_health(self):
        r = app.test_client().get("/health")
        self.assertEqual(r.status_code, 200)

    def test_message(self):
        r = app.test_client().get("/api/message")
        self.assertIn("message", r.get_json())

if __name__ == "__main__":
    unittest.main()
