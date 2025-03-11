import unittest
import logging
from src.model.progress import Progress

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TestProgress(unittest.TestCase):
    def test_track_progress(self):
        logging.info("🔹 Тест: отслеживание прогресса")
        progress = Progress()
        progress.add_progress("Кардио", "30 минут")

        with self.subTest(msg="Проверка истории тренировок"):
            self.assertIn("Кардио", progress.get_history())
            logging.info("Прогресс корректно сохраняется")

        logging.info("Тест пройден: прогресс успешно отслеживается!\n")
