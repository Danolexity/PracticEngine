import unittest
from src.model.nutrition import Nutrition

class TestNutrition(unittest.TestCase):
    def test_log_meal(self):
        nutrition = Nutrition()
        nutrition.log_meal("Овсянка", 350)
        
        self.assertEqual(len(nutrition.meals), 1)
        self.assertEqual(nutrition.meals[0]["name"], "Овсянка")
        self.assertEqual(nutrition.meals[0]["calories"], 350)

if __name__ == "__main__":
    unittest.main()
