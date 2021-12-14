from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        user = User.objects.get(pk=view.kwargs['pk'])

        return request.user == user