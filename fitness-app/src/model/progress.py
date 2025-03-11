from src.model.workout import Workout

"""Константы для сообщений об ошибках и форматирования"""
ERROR_EXPECTED_WORKOUT = "Ожидался объект Workout"
WORKOUT_MINUTES_LABEL = "минут"


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

    def get_history(self) -> list:
        """
        Получает список всех завершенных тренировок.

        :return: Список строк с описанием тренировок.
        """
        return [f"{w.workout_type}, {w.duration} {WORKOUT_MINUTES_LABEL}"
                for w in self.history]
