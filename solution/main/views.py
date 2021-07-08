from django.shortcuts import render
from django.views.generic import View
from .models import (ImgSingleHome, TextTextTextSingleHome, IntCharGroupAbout, 
CustomersGroupAbout, ImgTextTextGroupAbout, LogoGroupAboutNews, 
TextTextTextSingleServices, ImgTextTextGroupServices1, ImgTextTextGroupServices2, TextSinglesNews, 
ImgTextTextGroupNews)

class HomeView(View):
    def get(self, request):
        data1 = ImgSingleHome.objects.all()
        data2 = TextTextTextSingleHome.objects.all()
        return render(request, template_name="main/home.html",
        context={"data1": data1, "data2": data2})

class ServicesView(View):
    def get(self, request):
    
        data1 = TextTextTextSingleServices.objects.all()
        data2 = ImgTextTextGroupServices1.objects.all()
        data3 = ImgTextTextGroupServices2.objects.all()
        return render(request, template_name="main/services.html", 
        context={"data1": data1, "data2": data2, "data3": data3})


class AboutView(View):
    def get(self, request):
        data1 = IntCharGroupAbout.objects.all()
        data2 = CustomersGroupAbout.objects.all()
        data3 = ImgTextTextGroupAbout.objects.all()
        data5 = LogoGroupAboutNews.objects.all()
        return render(request, template_name="main/about.html",
        context={"data1": data1, "data2": data2, "data3": data3, "data5": data5})



class NewsView(View):
    def get(self, request):
        data2 = TextSinglesNews.objects.first()
        data3 = ImgTextTextGroupNews.objects.all()  
        return render(request, template_name="main/news.html",
        context={"data2": data2, "data3": data3})