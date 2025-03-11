import unittest
from src.model.user import User

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User("Test", 22, "test@mail.com")
        
        self.assertEqual(user.name, "Test")
        self.assertEqual(user.age, 22)
        self.assertEqual(user.email, "test@mail.com")

if __name__ == "__main__":
    unittest.main()
