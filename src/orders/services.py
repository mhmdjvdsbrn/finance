from .models import Order
from users.models import BaseUser

from django.db import transaction
from django.db.models import QuerySet

@transaction.atomic
def create_order(*, user: BaseUser, service) -> dict:
    order = Order.objects.create(
        user=user, service=service
    )
    return order





