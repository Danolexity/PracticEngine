import unittest
import logging
from src.model.workout import Workout

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestWorkout(unittest.TestCase):
    def test_workout_init(self):
        logging.info("\n" + "=" * 60)
        logging.info("Тест: инициализация тренировки")
        logging.info("=" * 60)

        workout = Workout("Кардио", 30)

        with self.subTest(msg="Проверка типа тренировки"):
            self.assertEqual(workout.workout_type, "Кардио")
            logging.info(f"Тип тренировки корректный: {workout.workout_type}")

        with self.subTest(msg="Проверка длительности тренировки"):
            self.assertEqual(workout.duration, 30)
            logging.info(f"Длительность тренировки корректная:\
                         {workout.duration} минут")

        logging.info("Тест пройден: объект тренировки успешно создан")
        logging.info("=" * 60)


if __name__ == "__main__":
    unittest.main(verbosity=2)
