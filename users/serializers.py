from rest_framework import serializers

from users.models import User
from users.validators import CheckPassword


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""

    password = serializers.CharField(write_only=True)
    passwordConfirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "tg_username", "password", "passwordConfirm")
        validators = [CheckPassword()]

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
        fields = ('first_name', 'last_name', 'email', 'tg_username')
