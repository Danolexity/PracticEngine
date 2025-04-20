from src.constants import *
from src.validators import validate_workout_type, validate_calories

class Workout:
    """Класс для представления тренировки."""

    def __init__(self, workout_type: str, duration: int):
        if duration <= 0:
            raise ValueError(ERROR_INVALID_DURATION)
        validate_workout_type(workout_type)

        self.workout_type = workout_type
        self.duration = duration

    def start_workout(self) -> str:
        return f"{WORKOUT_START_MESSAGE}: {self.workout_type}, {WORKOUT_DURATION_LABEL}: {self.duration} минут"
