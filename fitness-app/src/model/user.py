"""Константы для сообщений об ошибках"""
ERROR_EMPTY_NAME = "Имя не может быть пустым"
ERROR_INVALID_AGE = "Возраст должен быть положительным числом"
ERROR_INVALID_EMAIL = "Некорректный email"


class User:
    """Класс для управления профилем пользователя."""

    def __init__(self, name: str, age: int, email: str):
        """
        Создает профиль пользователя.
        :param name: Имя пользователя.
        :param age: Возраст пользователя.
        :param email: Email пользователя.
        :raises ValueError: Если имя пустое,
        возраст < 0, или email некорректный.
        """
        if not name.strip():
            raise ValueError(ERROR_EMPTY_NAME)
        if age <= 0:
            raise ValueError(ERROR_INVALID_AGE)
        if "@" not in email:
            raise ValueError(ERROR_INVALID_EMAIL)

        self.name = name
        self.age = age
        self.email = email

    def display_info(self) -> str:
        """
        Возвращает строку с информацией о пользователе.
        :return: Информация о пользователе.
        """
        return f"Имя: {self.name}, Возраст: {self.age}, Email: {self.email}"
