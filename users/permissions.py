from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_active:
            return True
        return False
