from rest_framework import permissions
import datetime
from orders.models import Order
from django.db.models.query import F, Q

class HasSuspiciousView(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            has_bronze_user = Order.objects.filter(
                Q(service__plan_name="G") | Q(service__plan_name="S") | Q(service__plan_name="B"),
                user=user,
                end_time__gte = datetime.datetime.now(),
            ).exists()
            return has_bronze_user
        return False


class HasSmartMoneyInflowView(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            has_bronze_user = Order.objects.filter(
                Q(service__plan_name="G") | Q(service__plan_name="S") ,
                user=user,
                end_time__gte = datetime.datetime.now(),
            ).exists()
            return has_bronze_user
        return False


class HasSmartMoneyOutflowView(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            has_bronze_user = Order.objects.filter(
                service__plan_name="G",
                user=user,
                end_time__gte = datetime.datetime.now(),
            ).exists()
            return has_bronze_user
        return False