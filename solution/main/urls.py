from .views import MainView, ServicesView, AboutView, NewsView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomLoginForm

urlpatterns = [
    path("", MainView.as_view(), name="home_view"),
    path("services/", ServicesView.as_view(), name="services_view"),
    path("about/", AboutView.as_view(), name="about_view"),
    path("news/", NewsView.as_view(), name="news_view"),
]
