from django.db import models

class ImgSingleHome(models.Model):
    img_path = models.CharField(max_length=100)

class TextTextTextSingleHome(models.Model):
    header = models.TextField()
    definition1 = models.TextField()
    definition2 = models.TextField()



class TextTextTextSingleServices(models.Model):
    header1 = models.TextField()
    header2 = models.TextField()
    definition = models.TextField()

class ImgTextTextGroupServices1(models.Model):
    img_path = models.CharField(max_length=100)
    title = models.TextField()
    text = models.TextField()

class ImgTextTextGroupServices2(models.Model):
    img_path = models.CharField(max_length=100)
    title = models.TextField()
    text = models.TextField()




class IntCharGroupAbout(models.Model):
    header = models.IntegerField()
    text = models.CharField(max_length=100)

class CustomersGroupAbout(models.Model):
    img_path = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    definition = models.TextField()

class ImgTextTextGroupAbout(models.Model):
    img_path = models.CharField(max_length=100)
    header = models.TextField()
    text = models.TextField()

class LogoGroupAboutNews(models.Model):
    logo_path = models.CharField(max_length=100)




class TextSinglesNews(models.Model):
    text = models.TextField()

class ImgTextTextGroupNews(models.Model):
    img_path = models.CharField(max_length=100)
    header = models.TextField()
    definition = models.TextField()






# class Client5(models.Model):

    # data_created = models.DateTimeField(default=timezone.now)

def  fullname(self):
    return self.img_path

def __str__(self) -> str:
    return self.fullname()








