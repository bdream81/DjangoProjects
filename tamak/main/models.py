from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Feedback(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()    
    date_published =  models.DateTimeField(default=timezone.now)
        

    def __str__(self) -> str:
        return self.text
        
    def get_absolute_url(self):
        return reverse('feedback_details', kwargs={'pk': self.pk})

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, verbose_name="Комментарий к отзыву")
    body = models.TextField(max_length=256, verbose_name="Комментарий")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.body

class UserProfile(models.Model):
    django_user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="user_profile"
        )
    user_image = models.ImageField(upload_to="user_profiles", default='user_profiles/default.jpg')

    def __str__(self) -> str:
        return self.django_user.username

