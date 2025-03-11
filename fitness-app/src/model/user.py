class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Email: {self.email}")
