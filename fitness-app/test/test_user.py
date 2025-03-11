import unittest
import logging
from src.model.user import User

logging.basicConfig(level=logging.INFO, format="%(message)s")

class TestUser(unittest.TestCase):
    def test_create_user(self):
        logging.info("\nТест: создание пользователя")

        user = User("Иван", 25, "ivan@mail.com")

        with self.subTest(msg="Проверка имени пользователя"):
            self.assertEqual(user.name, "Иван")
            logging.info("Имя пользователя корректное")

        with self.subTest(msg="Проверка возраста пользователя"):
            self.assertEqual(user.age, 25)
            logging.info("Возраст пользователя корректный")

        with self.subTest(msg="Проверка email пользователя"):
            self.assertEqual(user.email, "ivan@mail.com")
            logging.info("Email пользователя корректный")

        logging.info("Тест пройден: пользователь успешно создан")

if __name__ == "__main__":
    unittest.main(verbosity=2)
