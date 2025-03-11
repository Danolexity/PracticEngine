import unittest
import logging
from src.model.nutrition import Nutrition

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TestNutrition(unittest.TestCase):
    def test_add_food(self):
        logging.info("=" * 50)
        logging.info("🔹 Тест: добавление еды в дневник питания")
        nutrition = Nutrition()
        nutrition.add_food("Овсянка", 350)

        with self.subTest(msg="Проверка добавления калорий"):
            calories = nutrition.get_calories("Овсянка")
            logging.info(f"Получено: {calories} ккал (ожидалось: 350 ккал)")
            self.assertEqual(calories, 350)
            logging.info("Калорийность добавлена корректно")

        logging.info("Тест пройден: еда успешно добавлена в дневник!")
        logging.info("=" * 50 + "\n")

if __name__ == "__main__":
    unittest.main(verbosity=2)
