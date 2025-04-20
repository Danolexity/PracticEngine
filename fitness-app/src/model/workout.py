from src.constants import *

class Workout:
    """Класс для представления тренировки."""

    def __init__(self, workout_type: str, duration: int):
        """
        Инициализация тренировки.
        :param workout_type: Тип тренировки (например, Кардио, Силовая).
        :param duration: Длительность тренировки в минутах.
        :raises ValueError: Если длительность <= 0 или тип некорректный.
        """
        if duration <= 0:
            raise ValueError(ERROR_INVALID_DURATION)
        if workout_type not in ALLOWED_WORKOUT_TYPES:
            raise ValueError(f"{ERROR_INVALID_WORKOUT_TYPE}: {workout_type}")

        self.workout_type = workout_type
        self.duration = duration

    def start_workout(self) -> str:
        """
        Запускает тренировку.
        :return: Сообщение о начале тренировки.
        """
        return f"{WORKOUT_START_MESSAGE}: {self.workout_type}, {WORKOUT_DURATION_LABEL}: {self.duration} минут"
