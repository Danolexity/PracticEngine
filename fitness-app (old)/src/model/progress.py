from src.model.workout import Workout
from src.constants import *

class Progress:
    """Класс для отслеживания истории тренировок."""

    def __init__(self):
        """Инициализация списка для хранения истории тренировок."""
        self.history = []

    def add_progress(self, workout: Workout):
        """
        Добавляет тренировку в историю.
        :param workout: Объект тренировки.
        :raises TypeError: Если передан не объект Workout.
        """
        if not isinstance(workout, Workout):
            raise TypeError(ERROR_EXPECTED_WORKOUT)
        self.history.append(workout)

    def remove_workout(self, index: int):
        """
        Удаляет тренировку по индексу из истории.
        :param index: Индекс тренировки в списке.
        :raises IndexError: Если индекс некорректен.
        """
        if 0 <= index < len(self.history):
            del self.history[index]
        else:
            raise IndexError(ERROR_WORKOUT_INDEX)

    def edit_workout(self, index: int, new_workout: Workout):
        """
        Заменяет тренировку по указанному индексу на новую.
        :param index: Индекс редактируемой тренировки.
        :param new_workout: Новый объект Workout.
        :raises IndexError: Если индекс некорректен.
        """
        if 0 <= index < len(self.history):
            self.history[index] = new_workout
        else:
            raise IndexError(ERROR_WORKOUT_INDEX)

    def get_history(self) -> list:
        """
        Возвращает список всех завершенных тренировок в формате строк.
        :return: Список строк с описанием тренировок.
        """
        return [f"{w.workout_type}, {w.duration} {WORKOUT_MINUTES_LABEL}" for w in self.history]