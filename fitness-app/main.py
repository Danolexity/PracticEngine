from src.model.user import User
from src.model.workout import Workout
from src.model.nutrition import Nutrition
from src.model.progress import Progress

def main():
    user = User("Test", 22, "test@mail.com")
    workout = Workout("Кардио", 30)
    nutrition = Nutrition()
    progress = Progress()

    user.display_info()
    workout.start_workout()
    nutrition.log_meal("Овсянка", 350)
    progress.track_workout(workout)

if __name__ == "__main__":
    main()
