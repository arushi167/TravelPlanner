from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.index, name="home"),
    path("signup", views.signup, name="signup"),
]
