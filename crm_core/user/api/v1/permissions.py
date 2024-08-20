from rest_framework import permissions


class IsManagerOrCustomerManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=["manager", "customer_manager"]).exists()