from django.shortcuts import render, redirect
from django.views.generic import View
from .models import (ImgSingleHome, TextTextTextSingleHome, IntCharGroupAbout, 
CustomersGroupAbout, ImgTextTextGroupAbout, LogoGroupAboutNews, 
TextTextTextSingleServices, ImgTextTextGroupServices1, ImgTextTextGroupServices2, TextSinglesNews, 
ImgTextTextGroupNews)

from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(View):
    def get(self, request):
        login_form = CustomLoginForm()
        register_form = CustomUserCreationForm()
        data1 = ImgSingleHome.objects.all()
        data2 = TextTextTextSingleHome.objects.all()
        return render(request, template_name="main/home.html",
        context={"data1": data1, "data2": data2,  "login_form": login_form,
                "register_form": register_form})

    def post(self, request):
        register_form = CustomUserCreationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Your accont has been created successfully!")
            return redirect("login")
    
        messages.warning(request, register_form.error_messages)
        register_form = CustomUserCreationForm

class ServicesView(LoginRequiredMixin, View):

    def get(self, request):
    
        data1 = TextTextTextSingleServices.objects.all()
        data2 = ImgTextTextGroupServices1.objects.all()
        data3 = ImgTextTextGroupServices2.objects.all()
        return render(request, template_name="main/services.html", 
        context={"data1": data1, "data2": data2, "data3": data3})



class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        data1 = IntCharGroupAbout.objects.all()
        data2 = CustomersGroupAbout.objects.all()
        data3 = ImgTextTextGroupAbout.objects.all()
        data5 = LogoGroupAboutNews.objects.all()
        return render(request, template_name="main/about.html",
        context={"data1": data1, "data2": data2, "data3": data3, "data5": data5})

    def post(self, request):
        username = request.POST.get("full_name")
        from_email=request.POST.get("from_email")
        message_text=request.POST.get("message")

        subject=f'Обращение пользователя  {username}с сайта solution.com'
       
        try:
           
            send_mail(subject, message_text, from_email, recipient_list=[from_email])
            messages.success(request, 'Ваша заявка принята на обработку!')

        except BadHeaderError as e:
            messages.warning(request, e)

        return redirect('about_view')
        




class NewsView(LoginRequiredMixin, View):
    def get(self, request):
        data2 = TextSinglesNews.objects.first()
        data3 = ImgTextTextGroupNews.objects.all()  
        return render(request, template_name="main/news.html",
        context={"data2": data2, "data3": data3})
