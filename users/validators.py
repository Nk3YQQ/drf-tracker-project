from rest_framework.exceptions import ValidationError


class CheckPassword:
    """Валидатор проверяет совпадение паролей при регистрации пользователей"""

    def __call__(self, attrs):
        password = attrs.get("password")
        passwordConfirm = attrs.get("passwordConfirm")

        if password != passwordConfirm:
            raise ValidationError("Пароли не совпадают")

        return attrs
