class Progress:
    def __init__(self):
        self.history = []

    def add_progress(self, workout_type, duration):
        self.history.append(f"{workout_type}, {duration}")

    def get_history(self):
        return self.history
