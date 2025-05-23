import requests
import subprocess



API_URL = "http://127.0.0.1:8001/api"
access_token = None
refresh_token = None



def notify(message):
    subprocess.run(["python", "notify_bot.py", message])



def auth_headers():
    return {"Authorization": f"Bearer {access_token}"}


def refresh_access_token():
    global access_token, refresh_token
    response = requests.post(f"{API_URL}/auth/refresh/", json={
        "refresh": refresh_token
    })
    if response.status_code == 200:
        access_token = response.json()["access"]
        print("🔁 Токен обновлён.")
    else:
        print("❌ Не удалось обновить токен:", response.text)
        exit()


def protected_request(method, url, **kwargs):
    global access_token
    response = requests.request(method, url, headers=auth_headers(), **kwargs)
    if response.status_code == 401 and "token_not_valid" in response.text:
        print("⚠️ Токен просрочен. Обновляю...")
        refresh_access_token()
        response = requests.request(method, url, headers=auth_headers(), **kwargs)
    return response


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
        exit()


def login():
    global access_token, refresh_token
    print("\n=== Вход ===")
    username = input("Имя пользователя: ")
    password = input("Пароль: ")

    response = requests.post(f"{API_URL}/auth/login/", json={
        "username": username,
        "password": password
    })

    if response.status_code == 200:
        tokens = response.json()
        access_token = tokens["access"]
        refresh_token = tokens["refresh"]
        print("✅ Успешный вход.")
    else:
        print("❌ Ошибка входа:", response.text)
        exit()


def show_summary():
    user = protected_request("get", f"{API_URL}/auth/me/").json()
    workouts = protected_request("get", f"{API_URL}/workouts/").json()
    nutrition = protected_request("get", f"{API_URL}/nutrition/").json()

    total_duration = sum(w["duration"] for w in workouts)
    total_calories = sum(f["calories"] for f in nutrition)

    print(f"\n--- Отчёт для {user['username']} ---")
    print(f"Тренировок: {len(workouts)}, Общее время: {total_duration} минут")
    print(f"Продуктов: {len(nutrition)}, Съедено калорий: {total_calories}")


def list_items(endpoint):
    response = protected_request("get", f"{API_URL}/{endpoint}/")
    if response.status_code == 200:
        return response.json()
    else:
        print("❌ Ошибка:", response.text)
        exit()


def add_workout():
    print("\n=== Добавление тренировки ===")
    print("Доступные типы: Кардио, Силовая, Йога, Плавание, Бег")
    workout_type = input("Тип тренировки: ")
    duration = input("Длительность (мин): ")

    response = protected_request("post", f"{API_URL}/workouts/", json={
        "workout_type": workout_type,
        "duration": duration
    })

    if response.status_code == 201:
        print("✅ Тренировка добавлена.")
        notify(f"Добавлена тренировка: {workout_type}, {duration} мин.")
    else:
        print("❌ Ошибка:", response.text)
        exit()


def edit_workout():
    print("\n=== Редактирование тренировки ===")
    workouts = list_items("workouts")
    for w in workouts:
        print(f"{w['id']}: {w['workout_type']}, {w['duration']} мин")

    workout_id = input("Введите ID тренировки для редактирования: ")
    new_type = input("Новый тип тренировки: ")
    new_duration = input("Новая длительность (мин): ")

    response = protected_request("patch", f"{API_URL}/workouts/{workout_id}/", json={
        "workout_type": new_type,
        "duration": new_duration
    })

    if response.status_code == 200:
        print("✅ Тренировка обновлена.")
        notify(f"Обновлена тренировка ID {workout_id}: {new_type}, {new_duration} мин.")
    else:
        print("❌ Ошибка:", response.text)
        exit()


def delete_workout():
    print("\n=== Удаление тренировки ===")
    workouts = list_items("workouts")
    for w in workouts:
        print(f"{w['id']}: {w['workout_type']}, {w['duration']} мин")

    workout_id = input("Введите ID тренировки для удаления: ")

    response = protected_request("delete", f"{API_URL}/workouts/{workout_id}/")
    if response.status_code == 204:
        print("✅ Тренировка удалена.")
        notify(f"Удалена тренировка ID {workout_id}.")
    else:
        print("❌ Ошибка:", response.text)
        exit()



def add_food():
    print("\n=== Добавление еды ===")
    name = input("Название продукта: ")
    calories = input("Калории: ")

    response = protected_request("post", f"{API_URL}/nutrition/", json={
        "name": name,
        "calories": calories
    })

    if response.status_code == 201:
        print("✅ Продукт добавлен.")
        notify(f"Добавлен продукт: {name}, {calories} ккал.")
    else:
        print("❌ Ошибка:", response.text)
        exit()


def edit_food():
    print("\n=== Редактирование еды ===")
    foods = list_items("nutrition")
    for f in foods:
        print(f"{f['id']}: {f['name']} - {f['calories']} ккал")

    food_id = input("Введите ID продукта для редактирования: ")
    new_name = input("Новое название: ")
    new_calories = input("Новая калорийность: ")

    response = protected_request("patch", f"{API_URL}/nutrition/{food_id}/", json={
        "name": new_name,
        "calories": new_calories
    })

    if response.status_code == 200:
        print("✅ Продукт обновлён.")
        notify(f"Обновлён продукт ID {food_id}: {new_name}, {new_calories} ккал.")
    else:
        print("❌ Ошибка:", response.text)
        exit()


def delete_food():
    print("\n=== Удаление еды ===")
    foods = list_items("nutrition")
    for f in foods:
        print(f"{f['id']}: {f['name']} - {f['calories']} ккал")

    food_id = input("Введите ID продукта для удаления: ")

    response = protected_request("delete", f"{API_URL}/nutrition/{food_id}/")
    if response.status_code == 204:
        print("✅ Продукт удалён.")
        notify(f"Удалён продукт ID {food_id}.")
    else:
        print("❌ Ошибка:", response.text)
        exit()



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
            access_token = None


if __name__ == "__main__":
    main_menu()
