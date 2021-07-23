from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, UserProfile



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created == True:
        UserProfile.objects.create(django_user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.user_profile.save() 