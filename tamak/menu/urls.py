from django.urls import path
from .views import PrimaryListView, PrimaryDetailView, WineListView, WineDetailView

urlpatterns = [
    path('meals/', PrimaryListView.as_view(), name='primary_meals'),
    path('meal/details/<int:pk>/', PrimaryDetailView.as_view(), name='meal_details'),
    path('wine/', WineListView.as_view(), name='wine'),
    path('wine/details/<int:pk>/', WineDetailView.as_view(), name='wine_details'),
   
]