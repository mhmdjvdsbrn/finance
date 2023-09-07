from rest_framework import permissions
from datetime import date
from orders.models import Order
from django.db.models.query import F, Q

class HasSuspiciousView(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            has_bronze_user = Order.objects.filter(
                Q(service__plan_name="G") | Q(service__plan_name="S") | Q(service__plan_name="B"),
                user=user,
            ).exists()
            return has_bronze_user
        return False
