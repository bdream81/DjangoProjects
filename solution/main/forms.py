from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Azatot",
            }
        ),
        label="Login:",
    )
    first_name = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Jhon",
            }
        ),
        label="First name:",
    )
    last_name = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Doe",
            }
        ),
        label="Last name:",
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "aria-describedby": "emailHelp",
                "class": "form-control",
                "placeholder": "Your First Name",
            }
        ),
        label="Email:",
    )

    password1 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "At least 8 characters",
            }
        ),
        label="Type password:",
    )
    password2 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Passwords MUST be the same",
            }
        ),
        label="Confirm password:",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control"}),
        label="Login:",
    )

    password = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control"}),
        label="Password:",
    )
