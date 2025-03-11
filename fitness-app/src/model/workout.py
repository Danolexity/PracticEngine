class Workout:
    def __init__(self, type, duration):
        self.type = type
        self.duration = duration

    def start_workout(self):
        print(f"Начинаем тренировку: {self.type}, Длительность: {self.duration} минут")
