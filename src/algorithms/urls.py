from django.urls import path
from .apis import  SuspiciousVolumeUserApi ,SmartMoneyInflowApi ,SmartMoneyOutflowApi

urlpatterns = [

    path('suspicious-volume/', SuspiciousVolumeUserApi.as_view(),name="suspicious-volume"),
    path('smart-money-inflow/', SmartMoneyInflowApi.as_view(),name="smart-money-inflow"),
    path('smart-money-outflow/', SmartMoneyOutflowApi.as_view(),name="smart-money-outflow"),

]

