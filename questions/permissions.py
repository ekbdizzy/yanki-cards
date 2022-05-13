from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Permission check for authority of theme."""

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'author'):
            return obj.author == request.user
        elif hasattr(obj, 'theme'):
            return obj.theme.author == request.user
        elif hasattr(obj, 'question'):
            return obj.question.theme.author == request.user


class IsPublicTheme(permissions.BasePermission):
    """Permission check theme is not private.
    If it's public (not is_private), access granted."""

    def has_object_permission(self, request, view, obj):
        return not obj.is_private
