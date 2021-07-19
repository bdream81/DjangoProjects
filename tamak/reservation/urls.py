from . import views
from django.urls import path
from reservation.views import ReservationCreateView, ReservationListView
urlpatterns = [
     path("create/", ReservationCreateView.as_view(template_name="reservation/reservations_create.html"), name="create"),
     path("list/", ReservationListView.as_view(template_name="reservation/reservations_list.html"), name="list"),
     
    
]
