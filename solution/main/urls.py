from django.contrib.auth.forms import AuthenticationForm
from .views import HomeView , ServicesView, AboutView, NewsView
from django.urls import path
from .forms import CustomLoginForm
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("", HomeView.as_view(), name="home_view"),
    path("login/", LoginView.as_view(template_name="main/home.html", authentication_form=CustomLoginForm), name='login'),
    path("logout/", LogoutView.as_view(template_name="main/logout.html"), name="logout"),
    path("about/", AboutView.as_view(), name="about_view"),
    path("services/", ServicesView.as_view(), name="services_view"),
    path("news/", NewsView.as_view(), name="news_view")
]
