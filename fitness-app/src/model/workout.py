"""Константы для сообщений об ошибках"""
ERROR_INVALID_DURATION = "Длительность тренировки должна быть больше 0 минут"
WORKOUT_START_MESSAGE = "Начинаем тренировку"
WORKOUT_DURATION_LABEL = "Длительность"


class Workout:
    """Класс для представления тренировки."""

    def __init__(self, workout_type: str, duration: int):
        """
        Инициализация тренировки.
        :param workout_type: Тип тренировки (например, Кардио, Силовая).
        :param duration: Длительность тренировки в минутах.
        :raises ValueError: Если длительность тренировки <= 0.
        """
        if duration <= 0:
            raise ValueError(ERROR_INVALID_DURATION)

        self.workout_type = workout_type
        self.duration = duration

    def start_workout(self) -> str:
        """
        Запускает тренировку.
        :return: Сообщение о начале тренировки.
        """
        return f"{WORKOUT_START_MESSAGE}: {self.workout_type},\
            {WORKOUT_DURATION_LABEL}: {self.duration} минут"
