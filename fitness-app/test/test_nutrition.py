import unittest
import logging
from src.model.nutrition import Nutrition

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TestNutrition(unittest.TestCase):
    def test_add_food(self):
        logging.info("🔹 Тест: добавление еды в дневник питания")
        nutrition = Nutrition()
        nutrition.add_food("Овсянка", 350)

        with self.subTest(msg="Проверка добавления калорийности"):
            self.assertEqual(nutrition.get_calories("Овсянка"), 350)
            logging.info("Калорийность добавлена корректно")

        logging.info("Тест пройден: еда успешно добавлена в дневник!\n")
