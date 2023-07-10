from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsAdminOrWriteOnly(BasePermission):

    def has_permission(self, request: Request, view):
        if request.method == 'POST':
            return True
        user = request.user
        return user.is_staff
