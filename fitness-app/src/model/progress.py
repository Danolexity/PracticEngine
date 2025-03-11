class Progress:
    def __init__(self):
        self.history = []

    def track_workout(self, workout):
        self.history.append(workout)
        print(f"Тренировка {workout.type} добавлена в историю")
