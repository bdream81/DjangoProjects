from django.db import models
from django.utils import timezone

class ImgPathSingle(models.Model):
    img_path = models.CharField(max_length=100)

class TextSingle(models.Model):
    header_single = models.TextField()
    text_single = models.TextField()

class TextGroup(models.Model):
    header = models.TextField()
    text = models.TextField()

class ImgTextGroup(models.Model):
    img_path = models.CharField(max_length=100)
    header = models.TextField()
    text = models.TextField()

class Group4(models.Model):
    img_path = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    definition = models.TextField()

class LogoGroup(models.Model):
    logo_path = models.CharField(max_length=100)



# class Client5(models.Model):

    # data_created = models.DateTimeField(default=timezone.now)

def  fullname(self):
    return self.img_path

def __str__(self) -> str:
    return self.fullname()
