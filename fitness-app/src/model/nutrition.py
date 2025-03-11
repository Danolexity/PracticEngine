"""Константы для сообщений об ошибках"""
ERROR_INVALID_CALORIES = "Калорийность должна быть положительным числом"


class Nutrition:
    """Класс для отслеживания питания и калорийности."""

    def __init__(self):
        """Инициализация словаря для хранения информации о еде."""
        self.food_log = {}

    def add_food(self, name: str, calories: int):
        """
        Добавляет еду и ее калорийность в дневник питания.
        :param name: Название продукта.
        :param calories: Количество калорий.
        :raises ValueError: Если калорийность <= 0.
        """
        if calories <= 0:
            raise ValueError(ERROR_INVALID_CALORIES)

        self.food_log[name] = self.food_log.get(name, 0) + calories

    def get_calories(self, name: str) -> int:
        """
        Получает калорийность указанного продукта.
        :param name: Название продукта.
        :return: Количество калорий.
        """
        return self.food_log.get(name, 0)

    def get_total_calories(self) -> int:
        """
        Подсчитывает общее количество калорий за день.
        :return: Общее количество калорий.
        """
        return sum(self.food_log.values())
