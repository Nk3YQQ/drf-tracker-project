from django.conf import settings
from rest_framework import serializers

from users.models import User
from users.validators import CheckPassword


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""

    password = serializers.CharField(write_only=True)
    passwordConfirm = serializers.CharField(write_only=True)

    tg_link = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password", "passwordConfirm", "tg_link")
        validators = [CheckPassword()]

    @staticmethod
    def get_tg_link(obj) -> str:
        """ Добавление временного поля для ссылки """
        bot_name = settings.BOT_NAME
        tg_token = obj.tg_token
        return f'https://t.me/{bot_name}?start={tg_token}'

    def create(self, validated_data):
        validated_data.pop("passwordConfirm")
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для пользователей """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
