from rest_framework import serializers
from .models import User, Workout, Nutrition
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "age"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "age", "password", "password2"]

    def validate(self, attrs):
        if len(attrs["username"]) < 3:
            raise serializers.ValidationError({"username": "Имя пользователя должно содержать минимум 3 символа."})
        if not attrs["username"].isalnum():
            raise serializers.ValidationError({"username": "Имя пользователя должно содержать только буквы и цифры."})

        if attrs["age"] < 18 or attrs["age"] > 120:
            raise serializers.ValidationError({"age": "Возраст должен быть от 18 до 120 лет."})

        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["id", "workout_type", "duration", "created_at"]


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = ["id", "name", "calories", "created_at"]

    def validate_calories(self, value):
        if not (0 <= value <= 3000):
            raise serializers.ValidationError("Калорийность должна быть от 0 до 3000.")
        return value
