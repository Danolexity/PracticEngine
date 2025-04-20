from src.constants import *

class Nutrition:
    """Класс для отслеживания питания и калорийности."""

    def __init__(self):
        """Словарь для хранения информации о еде."""
        self.food_log = {}

    def add_food(self, name: str, calories: int):
        """
        Добавляет еду и её калорийность в дневник питания.
        :param name: Название продукта.
        :param calories: Количество калорий.
        :raises ValueError: Если калорийность <= 0 или превышает лимит.
        """
        if calories <= 0 or calories > MAX_CALORIES:
            raise ValueError(ERROR_INVALID_CALORIES)
        self.food_log[name] = self.food_log.get(name, 0) + calories

    def remove_food(self, name: str):
        """
        Удаляет запись о продукте из дневника питания.
        :param name: Название продукта.
        :raises ValueError: Если продукт не найден.
        """
        if name in self.food_log:
            del self.food_log[name]
        else:
            raise ValueError(ERROR_FOOD_NOT_FOUND)

    def edit_food(self, name: str, new_calories: int):
        """
        Изменяет калорийность указанного продукта.
        :param name: Название продукта.
        :param new_calories: Новое количество калорий.
        :raises ValueError: Если продукт не найден или калории недопустимы.
        """
        if name in self.food_log:
            if new_calories <= 0 or new_calories > MAX_CALORIES:
                raise ValueError(ERROR_INVALID_CALORIES)
            self.food_log[name] = new_calories
        else:
            raise ValueError(ERROR_FOOD_NOT_FOUND)

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