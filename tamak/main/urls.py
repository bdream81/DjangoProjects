from django.urls import path
from .views import MainView, AboutView, FeedbackCreateView, FeedbackListView, FeedbackDetailView, FeedbackUpdateView, FeedbackDeleteView

urlpatterns = [
    path('', MainView.as_view(), name='main_main'),
    path('about/', AboutView.as_view(), name='about_view'),
    path('feedbacks/create/', FeedbackCreateView.as_view(), name='feedback_view'),
    path('feedbacks', FeedbackListView.as_view(), name='all_view'),
    path('details/<int:pk>/', FeedbackDetailView.as_view(), name='feedback_details'),
    path('update/<int:pk>/', FeedbackUpdateView.as_view(), name='feedback_update'),
    path('delete/<int:pk>/', FeedbackDeleteView.as_view(), name='feedback_delete'),

    
]
