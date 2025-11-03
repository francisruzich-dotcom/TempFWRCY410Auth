
import unittest
import os
import json
import hashlib
from unittest.mock import patch
from io import StringIO

from app import create_user, login

class TestAuthModule(unittest.TestCase):

    def setUp(self):
        """Set up a test users directory."""
        self.test_users_dir = "test_users"
        if not os.path.exists(self.test_users_dir):
            os.makedirs(self.test_users_dir)

        self.username = "testuser"
        self.name = "Test User"
        self.password = "password123"

    def tearDown(self):
        """Clean up the test users directory."""
        for f in os.listdir(self.test_users_dir):
            os.remove(os.path.join(self.test_users_dir, f))
        os.rmdir(self.test_users_dir)

    def test_create_user_success(self):
        """Test that a user is created successfully."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            create_user(self.username, self.name, self.password, self.test_users_dir)
            self.assertEqual(fake_out.getvalue().strip(), f"User '{self.username}' created successfully.")

        user_file = os.path.join(self.test_users_dir, f"{self.username}.json")
        self.assertTrue(os.path.exists(user_file))

        with open(user_file, "r") as f:
            user_data = json.load(f)
            self.assertEqual(user_data["username"], self.username)
            self.assertEqual(user_data["name"], self.name)

    def test_create_user_duplicate(self):
        """Test that creating a duplicate user fails."""
        with patch('sys.stdout', new=StringIO()):
            create_user(self.username, self.name, self.password, self.test_users_dir)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            create_user(self.username, self.name, self.password, self.test_users_dir)
            self.assertEqual(fake_out.getvalue().strip(), f"Error: User '{self.username}' already exists.")

    def test_login_success(self):
        """Test that a user can log in with the correct password."""
        with patch('sys.stdout', new=StringIO()):
            create_user(self.username, self.name, self.password, self.test_users_dir)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            login(self.username, self.password, self.test_users_dir)
            self.assertEqual(fake_out.getvalue().strip(), "Login successful!")

    def test_login_failure_wrong_password(self):
        """Test that login fails with the wrong password."""
        with patch('sys.stdout', new=StringIO()):
            create_user(self.username, self.name, self.password, self.test_users_dir)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            login(self.username, "wrongpassword", self.test_users_dir)
            self.assertEqual(fake_out.getvalue().strip(), "Login failed. Incorrect username or password.")

    def test_login_failure_user_not_found(self):
        """Test that login fails with a non-existent username."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            login("nonexistentuser", "password", self.test_users_dir)
            self.assertEqual(fake_out.getvalue().strip(), "Login failed. Incorrect username or password.")

    def test_hash_and_salt(self):
        """Test that the password hashing and salting works correctly."""
        with patch('sys.stdout', new=StringIO()):
            create_user(self.username, self.name, self.password, self.test_users_dir)

        user_file = os.path.join(self.test_users_dir, f"{self.username}.json")
        with open(user_file, "r") as f:
            user_data = json.load(f)
            salt = user_data["salt"]
            hashed_password = user_data["hashed_password"]

            self.assertEqual(hashlib.sha256((self.password + salt).encode()).hexdigest(), hashed_password)
            self.assertNotEqual(hashlib.sha256(("wrongpassword" + salt).encode()).hexdigest(), hashed_password)

if __name__ == "__main__":
    unittest.main()
