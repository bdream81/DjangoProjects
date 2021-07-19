from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import EmailInput, TextInput
from django.forms.widgets import PasswordInput
from .models import Comment


   
class CustomUserCreationForm(UserCreationForm):
    username=forms.CharField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField(widget=PasswordInput)
    password2=forms.CharField(widget=PasswordInput)

    class Meta:
        model= User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2'
            ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
