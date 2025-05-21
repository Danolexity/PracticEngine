import unittest
from src.model.user import User
from src.model.workout import Workout
from src.model.nutrition import Nutrition

class TestUserSummary(unittest.TestCase):
    def test_generate_summary(self):
        # Создаём пользователя
        user = User("Тест", 30, "test@example.com")

        # Добавляем 2 тренировки
        user.add_workout(Workout("Кардио", 20))
        user.add_workout(Workout("Силовая", 40))

        # Добавляем 2 продукта
        user.add_food("Яблоко", 80)
        user.add_food("Рис", 300)

        expected = "Всего тренировок: 2, Общее время: 60 мин, Съедено калорий: 380"
        self.assertEqual(user.generate_summary(), expected)

if __name__ == "__main__":
    unittest.main()
