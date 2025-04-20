# main.py
from src.model.user import User
from src.model.workout import Workout
from src.constants import *

def main():
    try:
        name = input("Введите имя пользователя: ").strip()
        age = int(input("Введите возраст: "))
        email = input("Введите email: ").strip()
        user = User(name, age, email)

        while True:
            print("\nМеню:")
            print("1. Добавить тренировку")
            print("2. Добавить продукт питания")
            print("3. Редактировать тренировку")
            print("4. Редактировать продукт питания")
            print("5. Удалить тренировку")
            print("6. Удалить продукт питания")
            print("7. Показать отчёт")
            print("8. Выйти")

            choice = input("Выберите действие: ")

            if choice == "1":
                print("\nДоступные типы тренировок:", ", ".join(ALLOWED_WORKOUT_TYPES))
                workout_type = input("Введите тип тренировки: ")
                duration = int(input("Введите длительность (в минутах): "))
                workout = Workout(workout_type, duration)
                user.add_workout(workout)
                print("Тренировка добавлена.")

            elif choice == "2":
                name = input("Введите название продукта: ")
                calories = int(input("Введите количество калорий: "))
                if calories <= 0 or calories > MAX_CALORIES:
                    raise ValueError(ERROR_INVALID_CALORIES)
                user.add_food(name, calories)
                print("Продукт добавлен.")

            elif choice == "3":
                if not user.progress.history:
                    print("Нет тренировок для редактирования.")
                    continue
                print("\nТекущие тренировки:")
                for i, workout in enumerate(user.progress.history):
                    print(f"{i}: {workout.workout_type}, {workout.duration} мин")
                index = int(input("Введите индекс тренировки: "))
                workout_type = input("Введите новый тип тренировки: ")
                duration = int(input("Введите новую длительность: "))
                new_workout = Workout(workout_type, duration)
                user.edit_workout(index, new_workout)
                print("Тренировка обновлена.")

            elif choice == "4":
                if not user.nutrition.food_log:
                    print("Нет продуктов для редактирования.")
                    continue
                print("\nТекущие продукты:")
                for food, cal in user.nutrition.food_log.items():
                    print(f"{food}: {cal} ккал")
                name = input("Введите название продукта: ")
                new_calories = int(input("Введите новую калорийность: "))
                if new_calories <= 0 or new_calories > MAX_CALORIES:
                    raise ValueError(ERROR_INVALID_CALORIES)
                user.edit_food(name, new_calories)
                print("Данные о продукте обновлены.")

            elif choice == "5":
                if not user.progress.history:
                    print("Нет тренировок для удаления.")
                    continue
                print("\nТекущие тренировки:")
                for i, workout in enumerate(user.progress.history):
                    print(f"{i}: {workout.workout_type}, {workout.duration} мин")
                index = int(input("Введите индекс тренировки для удаления: "))
                user.remove_workout(index)
                print("Тренировка удалена.")

            elif choice == "6":
                if not user.nutrition.food_log:
                    print("Нет продуктов для удаления.")
                    continue
                print("\nТекущие продукты:")
                for food, cal in user.nutrition.food_log.items():
                    print(f"{food}: {cal} ккал")
                name = input("Введите название продукта для удаления: ")
                user.remove_food(name)
                print("Продукт удалён.")

            elif choice == "7":
                print("\n--- Отчёт ---")
                print(user.generate_summary())

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
