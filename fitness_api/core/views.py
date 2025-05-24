from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from .models import WORKOUT_TYPES


from .models import Workout, Nutrition, User
from .serializers import (
    WorkoutSerializer,
    NutritionSerializer,
    UserSerializer,
    RegisterSerializer
)


# Регистрация нового пользователя
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# Получение информации о текущем пользователе
class CurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# ViewSet для тренировок
class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ViewSet для питания
class NutritionViewSet(viewsets.ModelViewSet):
    serializer_class = NutritionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['GET'])
def workout_types(request):
    return Response([t[0] for t in WORKOUT_TYPES])
