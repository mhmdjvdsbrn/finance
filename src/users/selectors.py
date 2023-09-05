from django.db.models import QuerySet
from .models import BaseUser 

# def get_profile(user:BaseUser)->Profile:
#     return Profile.objects.get(user=user)

def get_user(pk)->BaseUser:
    query = BaseUser.objects.get(pk=pk)
    return query