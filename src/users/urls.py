from django.urls import path
from .apis import RegisterApi  ,DetaiUser

urlpatterns = [
    path('admin/', RegisterApi.as_view(),name="register"),

    path('register/', RegisterApi.as_view(),name="register"),
    path('detail/', DetaiUser.as_view(),name="user"),
]