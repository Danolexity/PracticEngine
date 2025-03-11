class Nutrition:
    def __init__(self):
        self.meals = []

    def log_meal(self, name, calories):
        self.meals.append({"name": name, "calories": calories})
        print(f"Добавлено: {name}, {calories} ккал")
