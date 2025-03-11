class Nutrition:
    def __init__(self):
        self.food_log = {}

    def add_food(self, name, calories):
        self.food_log[name] = calories

    def get_calories(self, name):
        return self.food_log.get(name, 0)
