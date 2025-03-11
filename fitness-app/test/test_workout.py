import unittest
import logging
from src.model.workout import Workout

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TestWorkout(unittest.TestCase):
    def test_workout_init(self):
        logging.info("=" * 50)
        logging.info("🔹 Тест: инициализация тренировки")
        workout = Workout("Кардио", 30)

        with self.subTest(msg="Проверка типа тренировки"):
            self.assertEqual(workout.type, "Кардио")
            logging.info("Тип тренировки корректный: Кардио")

        with self.subTest(msg="Проверка длительности тренировки"):
            self.assertEqual(workout.duration, 30)
            logging.info("Длительность тренировки корректная: 30 минут")

        logging.info("Тест пройден: объект тренировки успешно создан!")
        logging.info("=" * 50 + "\n")

if __name__ == "__main__":
    unittest.main(verbosity=2)
