from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import EmailInput, TextInput


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=TextInput)
    last_name = forms.CharField(widget=TextInput)
    email = forms.EmailField(widget=EmailInput)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
