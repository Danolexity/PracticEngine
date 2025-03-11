import unittest
from src.model.workout import Workout

class TestWorkout(unittest.TestCase):
    def test_workout_init(self):
        workout = Workout("Кардио", 30)
        
        self.assertEqual(workout.type, "Кардио")
        self.assertEqual(workout.duration, 30)

if __name__ == "__main__":
    unittest.main()
