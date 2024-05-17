from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """Проверка текущего пользователя на владельца аккаунта"""

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsUserOrReadOnly(permissions.BasePermission):
    """Проверка текущего пользователя на владельца аккаунта, либо разрешено только чтение"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user
