from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

class PrimaryMeal(models.Model):
    STARS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    name_bluda = models.CharField(max_length=100, verbose_name="Название блюда:")
    kitchen_bluda = models.CharField(max_length=100, verbose_name="Кухня:")
    opisanie_bluda = models.TextField(max_length=300, verbose_name="Описание, история")
    ocenka_bluda = models.CharField(choices=STARS, max_length=30, verbose_name="Оценка:")
    ingredients= models.CharField(max_length=250, verbose_name="Ингредиенты:")
    price_bluda = models.CharField(max_length=20, verbose_name="Цена:")
    image_bluda = models.CharField(max_length=200, verbose_name="Картинка:")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name_bluda

    def get_absolute_url(self):
        return reverse('meal_details')

class GeneralMeal(models.Model):
    KATEGORY = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    name_bluda = models.CharField(max_length=100, verbose_name="Название блюда:")
    image_bluda = models.CharField(max_length=200, verbose_name="Картинка:")
    price_bluda = models.CharField(max_length=20, verbose_name="Цена:")
    kategory = models.CharField(choices=KATEGORY, max_length=30, verbose_name="Категория:")
    opisanie_bluda = models.TextField(max_length=256, verbose_name="Описание:")
    aktual_date_bluda = models.DateTimeField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name_bluda

    def get_absolute_url(self):
        return reverse('meal_details')
    
class Wine(models.Model):
    KATEGORY = (
        ('Сладкое', 'Сладкое'),
        ('Полу-сладкое', 'Полу-сладкое'),
        ('Сухое', 'Сухое'),
        ('Полу-сухое', 'Полу-сухое')

    )

    COLOR = (
        ('Розовое', 'Розовое'),
        ('Белое', 'Белое'),
        ('Красное', 'Красное')
    )
    TYPE_WINA = (
        ('1', '1'),
        ('2', '2')
    )

    name_wina = models.CharField(max_length=100, verbose_name="Назмание вина:")
    image_wina = models.CharField(max_length=200, verbose_name="Картинка:")
    opisanie_wina = models.TextField(max_length=256, verbose_name="Описание:")
    type_wina = models.CharField(choices=TYPE_WINA, max_length=30, verbose_name="Тип:")
    kategory = models.CharField(choices=KATEGORY, max_length=30, verbose_name="Категория:")
    color = models.CharField(choices=COLOR, max_length=30, verbose_name="Цвет:")
    production = models.CharField(max_length=100, verbose_name="Производство:")
    price_wina = models.CharField(max_length=20, verbose_name="Цена:")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name_wina

    def get_absolute_url(self):
        return reverse('wine_details')
   
   