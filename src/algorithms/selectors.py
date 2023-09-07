from django.db.models import QuerySet
from users.models import BaseUser
from .models import SuspiciousVolume ,SmartMoneyInflow ,SmartMoneyOutflow


def show_suspicious_volume() -> QuerySet[SuspiciousVolume]:
    query = SuspiciousVolume.objects.order_by('-j_date')
    return query


def show_smart_money_inflow() -> QuerySet[SuspiciousVolume]:
    query = SmartMoneyInflow.objects.order_by('-j_date')
    return query



def show_smart_money_outflow() -> QuerySet[SuspiciousVolume]:
    query = SmartMoneyOutflow.objects.order_by('-j_date')
    return query