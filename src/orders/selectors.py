from django.db.models import QuerySet
from .models import Order
from users.models import BaseUser
from algorithms.models import SuspiciousVolume

def order_detail(user:BaseUser) -> QuerySet[Order]:
    query = Order.objects.get(user=user)
    return query


def show_suspicious_volume() -> QuerySet[SuspiciousVolume]:
    query = SuspiciousVolume.objects.order_by('-j_date')
    return query

