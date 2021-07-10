from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import CustomUserCreationForm


class MainView(View):
    def get(self, request):
        return render(request, template_name="main/main.html")


class RegistrationView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(
            request, template_name="main/registration.html", context={"form": form}
        )

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("main:about")

        form = CustomUserCreationForm()
        return render(request, template_name="main/login.html", context={"form": form})


class AboutView(View):
    def get(self, request):
        return render(request, template_name="main/about.html")
