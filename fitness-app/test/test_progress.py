import unittest
from src.model.progress import Progress
from src.model.workout import Workout

class TestProgress(unittest.TestCase):
    def test_track_workout(self):
        progress = Progress()
        workout = Workout("Кардио", 30)
        progress.track_workout(workout)
        
        self.assertEqual(len(progress.history), 1)
        self.assertEqual(progress.history[0].type, "Кардио")

if __name__ == "__main__":
    unittest.main()
