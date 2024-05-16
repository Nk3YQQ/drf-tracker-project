# Generated by Django 4.2 on 2024-05-16 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=200, verbose_name="Место")),
                ("time", models.TimeField(verbose_name="Время")),
                ("action", models.CharField(max_length=200, verbose_name="Действие")),
                (
                    "is_enjoyable",
                    models.BooleanField(default=False, verbose_name="Приятная привычка?"),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("hourly", "Каждый час"),
                            ("daily", "Ежедневно"),
                            ("weekly", "Еженедельно"),
                        ],
                        max_length=50,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "estimated_time",
                    models.PositiveIntegerField(verbose_name="Время на выполнение"),
                ),
                (
                    "is_public",
                    models.BooleanField(default=False, verbose_name="Привычка публичная?"),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habit.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "привычка",
                "verbose_name_plural": "привычки",
            },
        ),
    ]