from src.constants import *
from src.validators import validate_calories

class Nutrition:
    """Класс для отслеживания питания и калорийности."""

    def __init__(self):
        self.food_log = {}

    def add_food(self, name: str, calories: int):
        validate_calories(calories)
        self.food_log[name] = self.food_log.get(name, 0) + calories

    def remove_food(self, name: str):
        if name in self.food_log:
            del self.food_log[name]
        else:
            raise ValueError(ERROR_FOOD_NOT_FOUND)

    def edit_food(self, name: str, new_calories: int):
        if name in self.food_log:
            validate_calories(new_calories)
            self.food_log[name] = new_calories
        else:
            raise ValueError(ERROR_FOOD_NOT_FOUND)

    def get_calories(self, name: str) -> int:
        return self.food_log.get(name, 0)

    def get_total_calories(self) -> int:
        return sum(self.food_log.values())
