from django.db.models import QuerySet
from .models import Order
from users.models import BaseUser



def order_detail(user:BaseUser) -> QuerySet[Order]:
    query = Order.objects.get(user=user)
    return query