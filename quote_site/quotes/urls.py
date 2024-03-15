#tamplates/urls.py
from django.urls import path, include
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.home, name="home"), # quotes:home
 
    path("add_author", views.add_author, name="add_author"), 
    path("add_quote", views.add_quote, name="add_quote"),

]


