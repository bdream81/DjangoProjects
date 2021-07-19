
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Feedback, Comment
from .forms import CommentForm


class MainView(View):
    def get(self, request):
        return render(request, template_name='main/main.html')

class AboutView(View):
    def get(self, request):
        return render(request, template_name='main/about.html')


class RegistrationView(View):
    def get(self, request):
        register_form = CustomUserCreationForm()
        return render(request, template_name='main/registration.html',
        context={"register_form": register_form})

    def post(self, request):
        register_form = CustomUserCreationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
           
            return redirect("login")
    
       
        register_form = CustomUserCreationForm
        
        return render(request, template_name='main/registration.html',
        context={"register_form": register_form})


class FeedbackCreateView(CreateView):
    template_name='main/feedback_create.html'
    model = Feedback
    fields = [       
        'text',     
        ]

    def get_success_url(self) -> str:
        return reverse("feedback_details", kwargs={"pk": self.object.id})
        
    def form_valid(self, form):
        form.save(commit=False)
        form.instance.author = self.request.user
        form.save()
        return super(FeedbackCreateView, self).form_valid(form)

class FeedbackListView(ListView):
    template_name='main/feedback_list.html'
    model = Feedback

class FeedbackDetailView(DetailView):
    template_name='main/feedback_details.html'
    model = Feedback

    

    def get_context_data(self, **kwargs):
        form = CommentForm()
        feedback = self.get_object()

        feedback_comments = Comment.objects.filter(feedback=feedback).order_by("-date_created")
        kwargs["form"] = form
        kwargs["comments"] = feedback_comments
        return super().get_context_data(**kwargs)
    

   
    def post(self, request, pk, **kwargs):
        form = CommentForm(request.POST)
        form.save(commit=False)
        feedback = Feedback.objects.get(id=pk)

        feedback_comments = Comment.objects.filter(feedback=feedback).order_by("-date_created")

        form.instance.author = request.user
        form.instance.feedback = feedback


        if form.is_valid():
            form.save()
        form = CommentForm()
        return render(request, template_name="main/feedback_details.html", 
        context = {"form": form, "object": feedback})



class FeedbackUpdateView(UserPassesTestMixin, UpdateView):
    template_name = "main/feedback_update.html"
    model = Feedback
    fields = [
        "text"
        ]

    def test_func(self):
        feedback = self.get_object()
        if self.request.user == feedback.author:
            return True
        return False

class FeedbackDeleteView(UserPassesTestMixin, DeleteView):
    template_name = "main/feedback_delete.html"
    model = Feedback

    def get_success_url(self) -> str:
        return reverse('all_view')

    def test_func(self):
        feedback = self.get_object()
        if self.request.user == feedback.author:
            return True
        return False
