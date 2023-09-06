from django.urls import path
from .apis import BuyPlanApi ,DetailOrderApi ,UpdateOrderApi

urlpatterns = [
    path('new-order/', BuyPlanApi.as_view(),name="order"),
    path('detail-order/', DetailOrderApi.as_view(),name="order-detail"),
    path('detail-order/<int:order_id>/', UpdateOrderApi.as_view(), name='update-order'),


]