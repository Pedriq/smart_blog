from rest_framework import permissions


class IsOwner_or_IsStaff_or_ReadOnly(permissions.BasePermission):
    """
    Permission to change articles or blogs if
    the user is their creator or a user with rights
    staff
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user or request.user.is_staff
