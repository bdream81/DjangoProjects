from django.urls import path
from .views import MainView, AboutView

app_name = "main"

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("about/", AboutView.as_view(), name="about"),
]
