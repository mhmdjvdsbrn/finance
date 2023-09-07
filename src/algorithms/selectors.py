from django.db.models import QuerySet
from users.models import BaseUser
from .models import SuspiciousVolume


def show_suspicious_volume() -> QuerySet[SuspiciousVolume]:
    query = SuspiciousVolume.objects.order_by('-j_date')
    return query

