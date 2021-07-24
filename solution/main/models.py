from django.db import models

class ImgSingleHome(models.Model):
    img_path = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.img_path

class TextTextTextSingleHome(models.Model):
    header = models.TextField()
    definition1 = models.TextField()
    definition2 = models.TextField()

    def __str__(self) -> str:
        return self.header



class TextTextTextSingleServices(models.Model):
    header1 = models.TextField()
    header2 = models.TextField()
    definition = models.TextField()

    def __str__(self) -> str:
        return self.header1

class ImgTextTextGroupServices1(models.Model):
    img_path = models.CharField(max_length=100)
    title = models.TextField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.title

class ImgTextTextGroupServices2(models.Model):
    img_path = models.CharField(max_length=100)
    title = models.TextField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.title




class IntCharGroupAbout(models.Model):
    header = models.IntegerField()
    text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.header

class CustomersGroupAbout(models.Model):
    img_path = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    definition = models.TextField()

    def __str__(self) -> str:
        return self.name

class ImgTextTextGroupAbout(models.Model):
    img_path = models.CharField(max_length=100)
    header = models.TextField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.header

class LogoGroupAboutNews(models.Model):
    logo_path = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.logo_path




class TextSinglesNews(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text
    

class ImgTextTextGroupNews(models.Model):
    img_path = models.CharField(max_length=100)
    header = models.TextField()
    definition = models.TextField()

    def __str__(self) -> str:
        return self.header








