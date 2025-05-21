import requests

API_URL = "http://127.0.0.1:8001/api"
access_token = None


def auth_headers():
    return {"Authorization": f"Bearer {access_token}"}


def register():
    print("\n=== Регистрация ===")
    username = input("Имя пользователя: ")
    email = input("Email: ")
    age = input("Возраст: ")
    password = input("Пароль: ")
    password2 = input("Повторите пароль: ")

    response = requests.post(f"{API_URL}/auth/register/", json={
        "username": username,
        "email": email,
        "age": age,
        "password": password,
        "password2": password2
    })

    if response.status_code == 201:
        print("✅ Регистрация прошла успешно.")
    else:
        print("❌ Ошибка:", response.text)


def login():
    global access_token  # Меняем глобальную access_token, а не создаем новую
    print("\n=== Вход ===")
    username = input("Имя пользователя: ")
    password = input("Пароль: ")

    response = requests.post(f"{API_URL}/auth/login/", json={
        "username": username,
        "password": password
    })

    if response.status_code == 200:
        access_token = response.json()["access"]
        print("✅ Успешный вход.")
    else:
        print("❌ Ошибка входа:", response.text)


def show_summary():
    user = requests.get(f"{API_URL}/auth/me/", headers=auth_headers()).json()
    workouts = requests.get(f"{API_URL}/workouts/", headers=auth_headers()).json()
    nutrition = requests.get(f"{API_URL}/nutrition/", headers=auth_headers()).json()

    total_duration = sum(w["duration"] for w in workouts)
    total_calories = sum(f["calories"] for f in nutrition)

    print(f"\n--- Отчёт для {user['username']} ---")
    print(f"Тренировок: {len(workouts)}, Общее время: {total_duration} минут")
    print(f"Продуктов: {len(nutrition)}, Съедено калорий: {total_calories}")


def list_items(endpoint):
    response = requests.get(f"{API_URL}/{endpoint}/", headers=auth_headers())
    if response.status_code == 200:
        return response.json()
    else:
        print("❌ Ошибка:", response.text)
        return []


def add_workout():
    print("\n=== Добавление тренировки ===")
    print("Доступные типы: Кардио, Силовая, Йога, Плавание, Бег")
    workout_type = input("Тип тренировки: ")
    duration = input("Длительность (мин): ")

    response = requests.post(f"{API_URL}/workouts/", headers=auth_headers(), json={
        "workout_type": workout_type,
        "duration": duration
    })

    if response.status_code == 201:
        print("✅ Тренировка добавлена.")
    else:
        print("❌ Ошибка:", response.text)


def edit_workout():
    print("\n=== Редактирование тренировки ===")
    workouts = list_items("workouts")
    for w in workouts:
        print(f"{w['id']}: {w['workout_type']}, {w['duration']} мин")

    workout_id = input("Введите ID тренировки для редактирования: ")
    new_type = input("Новый тип тренировки: ")
    new_duration = input("Новая длительность (мин): ")

    response = requests.patch(f"{API_URL}/workouts/{workout_id}/", headers=auth_headers(), json={
        "workout_type": new_type,
        "duration": new_duration
    })

    if response.status_code == 200:
        print("✅ Тренировка обновлена.")
    else:
        print("❌ Ошибка:", response.text)


def delete_workout():
    print("\n=== Удаление тренировки ===")
    workouts = list_items("workouts")
    for w in workouts:
        print(f"{w['id']}: {w['workout_type']}, {w['duration']} мин")

    workout_id = input("Введите ID тренировки для удаления: ")

    response = requests.delete(f"{API_URL}/workouts/{workout_id}/", headers=auth_headers())
    if response.status_code == 204:
        print("✅ Тренировка удалена.")
    else:
        print("❌ Ошибка:", response.text)


def add_food():
    print("\n=== Добавление еды ===")
    name = input("Название продукта: ")
    calories = input("Калории: ")

    response = requests.post(f"{API_URL}/nutrition/", headers=auth_headers(), json={
        "name": name,
        "calories": calories
    })

    if response.status_code == 201:
        print("✅ Продукт добавлен.")
    else:
        print("❌ Ошибка:", response.text)


def edit_food():
    print("\n=== Редактирование еды ===")
    foods = list_items("nutrition")
    for f in foods:
        print(f"{f['id']}: {f['name']} - {f['calories']} ккал")

    food_id = input("Введите ID продукта для редактирования: ")
    new_name = input("Новое название: ")
    new_calories = input("Новая калорийность: ")

    response = requests.patch(f"{API_URL}/nutrition/{food_id}/", headers=auth_headers(), json={
        "name": new_name,
        "calories": new_calories
    })

    if response.status_code == 200:
        print("✅ Продукт обновлён.")
    else:
        print("❌ Ошибка:", response.text)


def delete_food():
    print("\n=== Удаление еды ===")
    foods = list_items("nutrition")
    for f in foods:
        print(f"{f['id']}: {f['name']} - {f['calories']} ккал")

    food_id = input("Введите ID продукта для удаления: ")

    response = requests.delete(f"{API_URL}/nutrition/{food_id}/", headers=auth_headers())
    if response.status_code == 204:
        print("✅ Продукт удалён.")
    else:
        print("❌ Ошибка:", response.text)


def authenticated_menu():
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

        choice = input("Выбор: ")
        if choice == "1":
            add_workout()
        elif choice == "2":
            add_food()
        elif choice == "3":
            edit_workout()
        elif choice == "4":
            edit_food()
        elif choice == "5":
            delete_workout()
        elif choice == "6":
            delete_food()
        elif choice == "7":
            show_summary()
        elif choice == "8":
            break
        else:
            print("Неверный выбор.")


def main_menu():
    while True:
        global access_token
        if access_token is None:
            print("\nДобро пожаловать!")
            print("1. Вход")
            print("2. Регистрация")
            print("3. Выход")
            choice = input("Выбор: ")
            if choice == "1":
                login()
            elif choice == "2":
                register()
            elif choice == "3":
                break
            else:
                print("Неверный выбор.")
        else:
            authenticated_menu()
            access_token = None  # сброс при выходе


if __name__ == "__main__":
    main_menu()
