from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Проверка пользователя на создателя привычки"""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверка пользователя на создателя привычки, либо разрешено только чтение"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
