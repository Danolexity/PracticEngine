from src.model.user import User
from src.model.workout import Workout
from src.model.nutrition import Nutrition
from src.model.progress import Progress

def main():
    try:
        user = User("Test", 22, "test@mail.com")
        workout = Workout("Кардио", 30)
        nutrition = Nutrition()
        progress = Progress()

        print(user.display_info())
        print(workout.start_workout())

        nutrition.add_food("Овсянка", 350)
        nutrition.add_food("Яблоко", 95)

        progress.add_progress(workout)

        print(f"Съедено калорий: {nutrition.get_total_calories()}")
        print("История тренировок:", progress.get_history())
    
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")

if __name__ == "__main__":
    main()
