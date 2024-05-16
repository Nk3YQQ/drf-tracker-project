from rest_framework import serializers

from habit.models import Habit
from habit.validators import CheckEnjoyableHabit, CheckRelatedHabit, CheckRelatedHabitAndReward, CheckTime


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели привычки"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [CheckRelatedHabitAndReward(), CheckTime(), CheckRelatedHabit(), CheckEnjoyableHabit()]
