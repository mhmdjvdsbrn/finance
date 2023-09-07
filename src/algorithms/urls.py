from django.urls import path
from .apis import  SuspiciousVolumeUserApi

urlpatterns = [

    path('suspicious-volume/', SuspiciousVolumeUserApi.as_view(),name="suspicious-volume"),

]