from django.urls import path
from .views import MainView, ServicesView, NewsView, AboutView
from main.forms import CustomLoginForm
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", MainView.as_view(), name="home_view"),
    path("services/", ServicesView.as_view(), name="services_view"),
    path("about/", AboutView.as_view(), name="about_view"),
    path("news/", NewsView.as_view(), name="news_view"),
    path(
        "login/",
        LoginView.as_view(
            template_name="main/home.html", authentication_form=CustomLoginForm
        ),
        name="login_view",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="main/logout.html"),
        name="logout_view",
    ),
]
