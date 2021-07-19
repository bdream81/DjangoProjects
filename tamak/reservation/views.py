
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, CreateView, ListView
from .models import Reservation
from django.views.generic.edit import FormView 
from .forms import ReservationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# class ReservationCreateView(CreateView):
#     template_name='reservation/reservations_create.html'
#     model = Reservation
#     fields = ["phon_number", 
#         "date_bron", 
#         "time_bron",
#         "person",
#         "comment"
#     ]
        
#     def form_valid(self, form):
#         form.save(commit=False)
#         form.instance.client = self.request.user
#         form.save()
#         return super(ReservationCreateView, self).form_valid(form)

class ReservationCreateView(LoginRequiredMixin, FormView):
    template_name='reservation/reservations_create.html'
    form_class = ReservationForm

    def get_success_url(self) -> str:
        return reverse("list")
    
    def form_valid(self, form):
        form.save(commit=False)
        form.instance.client = self.request.user
        form.save()
        return super(ReservationCreateView, self).form_valid(form)



class ReservationListView(LoginRequiredMixin, ListView):
    template_name='reservation/reservations_list.html'
    model = Reservation


    
