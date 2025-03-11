import unittest
import logging
from src.model.user import User

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TestUser(unittest.TestCase):
    def test_create_user(self):
        logging.info("🔹 Тест: создание пользователя")
        user = User("Alex", 25, "alex@example.com")

        with self.subTest(msg="Проверка имени пользователя"):
            self.assertEqual(user.name, "Alex")
            logging.info("Имя пользователя корректное")

        with self.subTest(msg="Проверка возраста пользователя"):
            self.assertEqual(user.age, 25)
            logging.info("Возраст пользователя корректный")

        with self.subTest(msg="Проверка email пользователя"):
            self.assertEqual(user.email, "alex@example.com")
            logging.info("Email пользователя корректный")

        logging.info("Тест пройден: пользователь успешно создан!\n")
