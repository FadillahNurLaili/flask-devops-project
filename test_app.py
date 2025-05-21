import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client()
        response = tester.get('/')
        assert response.status_code == 200

if __name__ == "__main__":
    unittest.main()
