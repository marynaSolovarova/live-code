# from django.contrib.auth import views as auth_views 
from django.urls import path, include
from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("", include('django.contrib.auth.urls')),
]
