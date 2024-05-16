from django.conf import settings
from django.db import models


class Periodicity(models.TextChoices):
    """Выбор периодичности"""

    DAILY = "daily", "Ежедневно"
    WEEKLY = "weekly", "Еженедельно"


class Habit(models.Model):
    """Модель привычки"""

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, **settings.NULLABLE, verbose_name="Пользователь")
    place = models.CharField(max_length=200, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=200, verbose_name="Действие")
    is_enjoyable = models.BooleanField(default=False, verbose_name="Приятная привычка?")
    related_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, **settings.NULLABLE, verbose_name="Связанная привычка"
    )
    periodicity = models.CharField(max_length=50, choices=Periodicity.choices, verbose_name="Периодичность")
    reward = models.CharField(max_length=200, **settings.NULLABLE, verbose_name="Вознаграждение")
    estimated_time = models.PositiveIntegerField(verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False, verbose_name="Привычка публичная?")

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
