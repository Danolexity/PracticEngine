import unittest
import logging
from src.model.progress import Progress

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TestProgress(unittest.TestCase):
    def test_track_progress(self):
        logging.info("=" * 50)
        logging.info("🔹 Тест: отслеживание прогресса")
        progress = Progress()
        progress.add_progress("Кардио", "30 минут")

        with self.subTest(msg="Проверка истории тренировок"):
            self.assertTrue(any("Кардио" in entry for entry in progress.get_history()))
            logging.info("Прогресс корректно сохраняется")

        logging.info("Тест пройден: прогресс успешно отслеживается!")
        logging.info("=" * 50 + "\n")

if __name__ == "__main__":
    unittest.main(verbosity=2)
