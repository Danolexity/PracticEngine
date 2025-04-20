""" Общие допустимые значения и сообщения """
MAX_CALORIES = 10000

""" Типы тренировок """
ALLOWED_WORKOUT_TYPES = {"Кардио", "Силовая", "Йога", "Плавание", "Бег"}

""" Сообщения об ошибках """
ERROR_INVALID_DURATION = "Длительность тренировки должна быть больше 0 минут"
ERROR_INVALID_WORKOUT_TYPE = "Недопустимый тип тренировки (Допустимые: Кардио, Силовая, ЙОга, Плавание, Бег)"
ERROR_INVALID_CALORIES = "Калорийность должна быть положительным числом"
ERROR_EMPTY_NAME = "Имя не может быть пустым"
ERROR_INVALID_AGE = "Возраст должен быть положительным числом"
ERROR_INVALID_EMAIL = "Некорректный email"
ERROR_EXPECTED_WORKOUT = "Ожидался объект Workout"
ERROR_FOOD_NOT_FOUND = "Продукт не найден"
ERROR_WORKOUT_INDEX = "Некорректный индекс тренировки"


""" Формат вывода """
WORKOUT_START_MESSAGE = "Начинаем тренировку"
WORKOUT_DURATION_LABEL = "Длительность"
WORKOUT_MINUTES_LABEL = "минут"
