from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CustomLoginForm, CustomUserCreationForm
from django.contrib import messages


class MainView(View):
    def get(self, request):
        login_form = CustomLoginForm()
        register_form = CustomUserCreationForm()
        return render(
            request,
            template_name="main/home.html",
            context={
                "login_form": login_form,
                "register_form": register_form,
            },
        )

    def post(self, request):
        register_form = CustomUserCreationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Your accont has been created successfully!")
            return redirect("login")

        messages.warning(request, register_form.error_messages)

        login_form = CustomLoginForm()
        register_form = CustomUserCreationForm()
        return render(
            request,
            template_name="main/home.html",
            context={
                "login_form": login_form,
                "register_form": register_form,
            },
        )


class AboutView(View):
    def get(self, request):
        return render(request, template_name="main/about.html")
