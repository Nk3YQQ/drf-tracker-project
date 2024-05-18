from django.conf import settings
from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsUser, IsUserOrReadOnly
from users.serializers import UserRegistrationSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""

    serializer_class = UserRegistrationSerializer

    @extend_schema(description='Отправление сообщения о продолжении регистрации')
    def perform_create(self, serializer):
        user = serializer.save()

        send_mail(
            subject='Добро пожаловать в приложение "E&I Habit Tracker!"',
            message=f"""Для продолжения регистрации перейдите в наш телеграмм-бот 
            https://t.me/{settings.BOT_NAME}?start={user.tg_token}""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return user


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Чтение одного пользователя """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserOrReadOnly]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Обновление пользователя """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUser]
