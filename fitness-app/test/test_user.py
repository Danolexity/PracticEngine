import unittest
import logging
from src.model.user import User

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TestUser(unittest.TestCase):
    def test_create_user(self):
        logging.info("=" * 50)
        logging.info("🔹 Тест: создание пользователя")
        user = User("test", 99, "test@mail.com")

        with self.subTest(msg="Проверка имени"):
            self.assertEqual(user.name, "test")
            logging.info("Имя пользователя корректное")

        with self.subTest(msg="Проверка возраста"):
            self.assertEqual(user.age, 99)
            logging.info("Возраст пользователя корректный")

        with self.subTest(msg="Проверка email"):
            self.assertEqual(user.email, "test@mail.com")
            logging.info("Email пользователя корректный")

        logging.info("Тест пройден: пользователь успешно создан!")
        logging.info("=" * 50 + "\n")

if __name__ == "__main__":
    unittest.main(verbosity=2)
