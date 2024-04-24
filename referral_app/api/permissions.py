from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        profile_owner = obj.id
        user = request.user.id
        return profile_owner == user
