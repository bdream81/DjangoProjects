
from django.db import models
from django.forms import forms
from django.shortcuts import render, reverse
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import GeneralMeal, PrimaryMeal, Wine


class PrimaryListView(ListView):
    template_name='menu/primary_meals.html'
    model = PrimaryMeal

    def get_context_data(self, **kwargs):
        breakfast = GeneralMeal.objects.filter(kategory = '1')
        lunch = GeneralMeal.objects.filter(kategory = '2')
        dinner = GeneralMeal.objects.filter(kategory = '3')
        kwargs['lunch'] = lunch
        kwargs['dinner'] = dinner
        kwargs['breakfast'] = breakfast
        return super().get_context_data(**kwargs)


class PrimaryDetailView(DetailView):
    template_name='menu/primary_details.html'
    model = PrimaryMeal


class WineListView(ListView):
    template_name='menu/wines.html'
    model = Wine

    def get_context_data(self, **kwargs):
        special = Wine.objects.filter(type_wina = '1')
        normal = Wine.objects.filter(type_wina = '2')
        kategory = Wine.objects.all
        color = Wine.objects.all
        kwargs['special'] = special
        kwargs['normal'] = normal
        kwargs['kategory'] = kategory
        kwargs['color'] = color
        return super().get_context_data(**kwargs)

class WineDetailView(DetailView):
    template_name='menu/wine_details.html'
    model = Wine
   
    

