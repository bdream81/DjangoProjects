from .views import MainView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", MainView.as_view(), name="main_view"),
]
