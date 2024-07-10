from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверят, является ли пользователь модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsOwner(permissions.BasePermission):
    """Проверят, является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsOwnProfile(permissions.BasePermission):
    """Проверяет, является ли пользователь владельцем профиля"""

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
