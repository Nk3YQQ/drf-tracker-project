from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")

    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    tg_username = models.CharField(unique=True, max_length=150, verbose_name="Имя пользователя в Телеграмме")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
