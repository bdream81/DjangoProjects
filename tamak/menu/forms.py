from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import EmailInput, TextInput
from django.forms.widgets import PasswordInput
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["opisanie_bluda"]