import unittest
import logging
from src.model.progress import Progress
from src.model.workout import Workout

logging.basicConfig(level=logging.INFO, format="%(message)s")

class TestProgress(unittest.TestCase):
    def test_track_progress(self):
        logging.info("\nТест: отслеживание прогресса")

        progress = Progress()
        workout = Workout("Кардио", 30)
        progress.add_progress(workout)

        expected_history = ["Кардио, 30 минут"]
        actual_history = progress.get_history()

        with self.subTest(msg="Проверка истории тренировок"):
            self.assertEqual(actual_history, expected_history)
            logging.info("Прогресс корректно сохраняется")

        logging.info("Тест пройден: прогресс успешно отслеживается")

if __name__ == "__main__":
    unittest.main(verbosity=2)
