from rest_framework.validators import ValidationError


class CheckRelatedHabitAndReward:
    """Валидатор для проверки связанной привычки и награды"""

    def __call__(self, attrs):
        related_habit = attrs.get("related_habit")
        reward = attrs.get("reward")

        if related_habit and reward:
            raise ValidationError("Поле 'полезная привычка' и 'награда' не могут быть заполнены одновременно")


class CheckTime:
    """Валидатор для проверки времени"""

    def __call__(self, attrs):
        estimated_time = attrs.get("estimated_time")

        if estimated_time and estimated_time > 120:
            raise ValidationError("Время не может быть больше 120 секунд")

        elif estimated_time and estimated_time < 0:
            raise ValidationError("Время не может быть отрицательным")


class CheckRelatedHabit:
    """Валидатор для проверки связанной привычки"""

    def __call__(self, attrs):
        related_habit = attrs.get("related_habit")

        if related_habit and not related_habit.is_enjoyable:
            raise ValidationError("Связанные привычки должны являться приятной привычкой")


class CheckEnjoyableHabit:
    """Валидатор для проверки приятной привычки"""

    def __call__(self, attrs):
        is_enjoyable = attrs.get("is_enjoyable")
        reward = attrs.get("reward")
        related_habit = attrs.get("related_habit")

        if is_enjoyable and (reward or related_habit):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")
