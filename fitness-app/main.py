from src.model.user import User
from src.model.workout import Workout
from src.constants import *
from src.validators import get_int_input

def print_menu():
    print("\nМеню:")
    print("1. Добавить тренировку")
    print("2. Добавить продукт питания")
    print("3. Редактировать тренировку")
    print("4. Редактировать продукт питания")
    print("5. Удалить тренировку")
    print("6. Удалить продукт питания")
    print("7. Показать отчёт")
    print("8. Выйти")

def add_workout(user):
    print("\nДоступные типы тренировок:", ", ".join(ALLOWED_WORKOUT_TYPES))
    workout_type = input("Введите тип тренировки: ")
    duration = get_int_input("Введите длительность (в минутах): ")
    user.add_workout(Workout(workout_type, duration))
    print("Новая тренировка добавлена.")

def add_food(user):
    name = input("Введите название продукта: ")
    calories = get_int_input("Введите количество калорий: ")
    user.add_food(name, calories)
    print("Продукт добавлен.")

def edit_workout(user):
    if not user.progress.history:
        print("Нет тренировок для редактирования.")
        return
    for i, workout in enumerate(user.progress.history):
        print(f"{i}: {workout.workout_type}, {workout.duration} мин")
    index = get_int_input("Введите индекс тренировки: ")
    workout_type = input("Введите новый тип тренировки: ")
    duration = get_int_input("Введите новую длительность: ")
    user.edit_workout(index, Workout(workout_type, duration))
    print("Тренировка обновлена.")

def edit_food(user):
    if not user.nutrition.food_log:
        print("Нет продуктов для редактирования.")
        return
    for food, cal in user.nutrition.food_log.items():
        print(f"{food}: {cal} ккал")
    name = input("Введите название продукта: ")
    new_calories = get_int_input("Введите новую калорийность: ")
    user.edit_food(name, new_calories)
    print("Данные о продукте обновлены.")

def remove_workout(user):
    if not user.progress.history:
        print("Нет тренировок для удаления.")
        return
    for i, workout in enumerate(user.progress.history):
        print(f"{i}: {workout.workout_type}, {workout.duration} мин")
    index = get_int_input("Введите индекс тренировки для удаления: ")
    user.remove_workout(index)
    print("Тренировка удалена.")

def remove_food(user):
    if not user.nutrition.food_log:
        print("Нет продуктов для удаления.")
        return
    for food, cal in user.nutrition.food_log.items():
        print(f"{food}: {cal} ккал")
    name = input("Введите название продукта для удаления: ")
    user.remove_food(name)
    print("Продукт удалён.")

def show_summary(user):
    print("\n--- Отчёт ---")
    print(user.generate_summary())

def main():
    try:
        user = User.create()
        while True:
            print_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                add_workout(user)
            elif choice == "2":
                add_food(user)
            elif choice == "3":
                edit_workout(user)
            elif choice == "4":
                edit_food(user)
            elif choice == "5":
                remove_workout(user)
            elif choice == "6":
                remove_food(user)
            elif choice == "7":
                show_summary(user)
            elif choice == "8":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
    except IndexError as e:
        print(f"Ошибка индекса: {e}")

if __name__ == "__main__":
    main()
