from src.model.workout import Workout

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
            raise TypeError("Ожидался объект Workout")
        self.history.append(workout)

    def get_history(self) -> list:
        """
        Получает список всех завершенных тренировок.
        :return: Список строк с описанием тренировок.
        """
        return [f"{w.workout_type}, {w.duration} минут" for w in self.history]
