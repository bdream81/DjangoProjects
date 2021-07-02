from django.urls import path
from .views import AboutView, HomeView, ServicesView, NewsView

urlpatterns = [
    path("about/", AboutView.as_view(), name="about_view"),
    path("home/", HomeView.as_view(), name="home_view"),
    path("services/", ServicesView.as_view(), name="services_view"),
    path("news/", NewsView.as_view(), name="news_view")
]
