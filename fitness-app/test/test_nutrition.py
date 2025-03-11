import unittest
import logging
from src.model.nutrition import Nutrition

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestNutrition(unittest.TestCase):
    def test_add_food(self):
        logging.info("\n" + "=" * 60)
        logging.info("Тест: добавление еды в дневник питания")
        logging.info("=" * 60)

        nutrition = Nutrition()
        nutrition.add_food("Овсянка", 350)

        expected_calories = 350
        actual_calories = nutrition.get_calories("Овсянка")

        with self.subTest(msg="Проверка добавления калорийности"):
            self.assertEqual(actual_calories, expected_calories)
            logging.info(f"Получено: {actual_calories} ккал\
                         (ожидалось: {expected_calories} ккал)")
            logging.info("Калорийность добавлена корректно")

        logging.info("Тест пройден: еда успешно добавлена в дневник")
        logging.info("=" * 60)


if __name__ == "__main__":
    unittest.main(verbosity=2)
