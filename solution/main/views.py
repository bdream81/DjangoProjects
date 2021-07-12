from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm, CustomLoginForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(View):
    def get(self, request):
        login_form = CustomLoginForm()
        sign_up_from = UserRegistrationForm()
        return render(
            request,
            template_name="main/home.html",
            context={"sign_up_from": sign_up_from, "login_form": login_form},
        )

    def post(self, request):
        sign_up_from = UserRegistrationForm(request.POST)
        if sign_up_from.is_valid():
            messages.success(request, f"You Registered successfully!")
            sign_up_from.save()
            return render(request, template_name="main/home.html")

        login_form = CustomLoginForm()
        sign_up_from = UserRegistrationForm()

        return render(
            request,
            template_name="wrapper.html",
            context={"sign_up_from": sign_up_from, "login_form": login_form},
        )


class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name="main/about.html")

    def post(self, request):
        username = request.POST.get("full_name")
        from_email = request.POST.get("from_email")
        message_text = request.POST.get("message")

        subject = f"Обращение пользователя {username} с сайта solution.com"

        try:
            send_mail(subject, message_text, from_email, recipient_list=[from_email])
            messages.success(request, "Ваша заявка принята на обработку!")
        except BadHeaderError as e:
            messages.warning(request, e)

        return redirect("about_view")


class ServicesView(LoginRequiredMixin, View):
    def get(self, request):
        login_form = CustomLoginForm()
        sign_up_from = UserRegistrationForm()
        return render(
            request,
            template_name="main/home.html",
            context={"sign_up_from": sign_up_from, "login_form": login_form},
        )


class NewsView(LoginRequiredMixin, View):
    def get(self, request):
        login_form = CustomLoginForm()
        sign_up_from = UserRegistrationForm()
        return render(
            request,
            template_name="main/home.html",
            context={"sign_up_from": sign_up_from, "login_form": login_form},
        )
