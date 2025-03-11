class User:
    """Класс для управления профилем пользователя."""
    
    def __init__(self, name: str, age: int, email: str):
        """
        Создает профиль пользователя.
        :param name: Имя пользователя.
        :param age: Возраст пользователя.
        :param email: Email пользователя.
        :raises ValueError: Если имя пустое, возраст < 0, или email некорректный.
        """
        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        if "@" not in email:
            raise ValueError("Некорректный email")

        self.name = name
        self.age = age
        self.email = email

    def display_info(self) -> str:
        """
        Возвращает строку с информацией о пользователе.
        :return: Информация о пользователе.
        """
        return f"Имя: {self.name}, Возраст: {self.age}, Email: {self.email}"
