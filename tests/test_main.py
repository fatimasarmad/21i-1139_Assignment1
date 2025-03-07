import unittest
import sys
import os

# Add the 'flask-ci-cd/app' directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../flask-ci-cd/app')))

from main import app  # Correctly import the Flask app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        """Set up a test client before each test"""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Test if the home route works"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
