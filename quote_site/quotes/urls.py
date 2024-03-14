from django.urls import path, include
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.home, name="home"), # quotes://home
]
