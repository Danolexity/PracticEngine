from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Типы тренировок — как choices
WORKOUT_TYPES = [
    ("Кардио", "Кардио"),
    ("Силовая", "Силовая"),
    ("Йога", "Йога"),
    ("Плавание", "Плавание"),
    ("Бег", "Бег"),
]

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["email", "age"]
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    workout_type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    duration = models.PositiveIntegerField(help_text="в минутах")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.workout_type} - {self.duration} мин."


class Nutrition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="foods")
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.calories} ккал"

