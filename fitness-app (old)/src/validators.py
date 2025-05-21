from src.constants import *
import re


def validate_calories(value: int):
    """
    Проверяет допустимость значения калорий.
    :param value: Значение калорий.
    :raises ValueError: Если значение вне допустимого диапазона.
    """
    if value <= 0 or value > MAX_CALORIES:
        raise ValueError(ERROR_INVALID_CALORIES)


def validate_workout_type(workout_type: str):
    """
    Проверяет корректность типа тренировки.
    :param workout_type: Тип тренировки.
    :raises ValueError: Если тип тренировки недопустим.
    """
    if workout_type not in ALLOWED_WORKOUT_TYPES:
        raise ValueError(f"{ERROR_INVALID_WORKOUT_TYPE}: {workout_type}")


def validate_age(age: int):
    """
    Проверка корректности возраста.
    :param age: Возраст пользователя.
    :raises ValueError: Если возраст недопустим.
    """
    if age <= 0 or age > 120:
        raise ValueError(ERROR_INVALID_AGE)


def validate_email(email: str):
    """
    Проверка формата email.
    :param email: Email пользователя.
    :raises ValueError: Если email некорректен.
    """
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError(ERROR_INVALID_EMAIL)


def get_int_input(prompt: str) -> int:
    """
    Безопасный ввод целого числа.
    :param prompt: Текст запроса ввода.
    :return: Введённое число.
    :raises ValueError: Если ввод не является числом.
    """
    try:
        return int(input(prompt))
    except ValueError:
        raise ValueError("Ожидалось целое число")
