from src.constants import *
from src.model.nutrition import Nutrition
from src.model.progress import Progress
from src.validators import validate_age, validate_email, get_int_input

class User:
    """Класс для управления профилем пользователя и его действиями."""

    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
        self.nutrition = Nutrition()
        self.progress = Progress()

    @classmethod
    def create(cls):
        name = input("Введите имя пользователя: ").strip()
        if not name:
            raise ValueError(ERROR_EMPTY_NAME)

        age = get_int_input("Введите возраст: ")
        validate_age(age)

        email = input("Введите email: ").strip()
        validate_email(email)

        return cls(name, age, email)

    def display_info(self) -> str:
        return f"Имя: {self.name}, Возраст: {self.age}, Email: {self.email}"

    def add_workout(self, workout):
        self.progress.add_progress(workout)

    def edit_workout(self, index: int, new_workout):
        self.progress.edit_workout(index, new_workout)

    def remove_workout(self, index: int):
        self.progress.remove_workout(index)

    def add_food(self, name, calories):
        self.nutrition.add_food(name, calories)

    def edit_food(self, name, new_calories):
        self.nutrition.edit_food(name, new_calories)

    def remove_food(self, name):
        self.nutrition.remove_food(name)

    def get_total_food_calories(self):
        return self.nutrition.get_total_calories()

    def generate_summary(self):
        total_duration = sum([w.duration for w in self.progress.history])
        return f"Всего тренировок: {len(self.progress.history)}, Общее время: {total_duration} мин, Съедено калорий: {self.get_total_food_calories()}"
