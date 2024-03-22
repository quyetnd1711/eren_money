from django.urls import path

from . import views

urlpatterns = [
    path("", views.gold, name="index"),
    path("gold", views.gold, name="gold"),
]