from django.urls import path
from .apis import RegisterApi 

urlpatterns = [
    path('register/', RegisterApi.as_view(),name="register"),
    # path('profile/', ProfileApi.as_view(),name="profile"),

]