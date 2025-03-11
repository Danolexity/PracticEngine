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
            raise ValueError("Длительность тренировки должна быть больше 0 минут")

        self.workout_type = workout_type
        self.duration = duration

    def start_workout(self) -> str:
        """
        Запускает тренировку.
        :return: Сообщение о начале тренировки.
        """
        return f"Начинаем тренировку: {self.workout_type}, Длительность: {self.duration} минут"
