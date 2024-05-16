from rest_framework import generics

from users.serializers import UserRegistrationSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""

    serializer_class = UserRegistrationSerializer
