import re
from src.constants import *
from src.model.nutrition import Nutrition
from src.model.progress import Progress

class User:
    """Класс для управления профилем пользователя и его действиями."""

    def __init__(self, name: str, age: int, email: str):
        """
        Инициализация профиля пользователя.
        :param name: Имя пользователя.
        :param age: Возраст пользователя.
        :param email: Email пользователя.
        :raises ValueError: Если данные некорректны.
        """
        if not name.strip():
            raise ValueError(ERROR_EMPTY_NAME)
        if age <= 0 or age > 120:
            raise ValueError(ERROR_INVALID_AGE)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError(ERROR_INVALID_EMAIL)

        self.name = name
        self.age = age
        self.email = email
        self.nutrition = Nutrition()
        self.progress = Progress()

    def display_info(self) -> str:
        """
        Возвращает информацию о пользователе.
        :return: Строка с именем, возрастом и email.
        """
        return f"Имя: {self.name}, Возраст: {self.age}, Email: {self.email}"

    def add_workout(self, workout):
        """
        Добавляет тренировку в историю пользователя.
        :param workout: Объект тренировки.
        """
        self.progress.add_progress(workout)

    def edit_workout(self, index: int, new_workout):
        """
        Редактирует тренировку пользователя.
        :param index: Индекс тренировки.
        :param new_workout: Новый объект тренировки.
        """
        self.progress.edit_workout(index, new_workout)

    def remove_workout(self, index: int):
        """
        Удаляет тренировку по индексу.
        :param index: Индекс удаляемой тренировки.
        """
        self.progress.remove_workout(index)

    def add_food(self, name, calories):
        """
        Добавляет приём пищи пользователю.
        :param name: Название продукта.
        :param calories: Калорийность.
        """
        self.nutrition.add_food(name, calories)

    def edit_food(self, name, new_calories):
        """
        Редактирует калорийность продукта.
        :param name: Название продукта.
        :param new_calories: Новое количество калорий.
        """
        self.nutrition.edit_food(name, new_calories)

    def remove_food(self, name):
        """
        Удаляет продукт из питания пользователя.
        :param name: Название продукта.
        """
        self.nutrition.remove_food(name)

    def get_total_food_calories(self):
        """
        Возвращает общее количество калорий за день.
        :return: Сумма калорий.
        """
        return self.nutrition.get_total_calories()

    def generate_summary(self):
        """
        Формирует краткий отчёт по активности пользователя.
        :return: Строка с количеством тренировок, общей длительностью и съеденными калориями.
        """
        total_duration = sum([w.duration for w in self.progress.history])
        return f"Всего тренировок: {len(self.progress.history)}, Общее время: {total_duration} мин, Съедено калорий: {self.get_total_food_calories()}"
