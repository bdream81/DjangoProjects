from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, TextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.shortcuts import reverse

class Reservation(models.Model):
    
    AMOUNT_PERSON = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12')
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    phon_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    date_bron = models.DateField(verbose_name="Дата бронирования")
    time_bron = models.TimeField(verbose_name="Время бронирования")
    person = models.CharField(
        choices=AMOUNT_PERSON,
        default=AMOUNT_PERSON[0][0],
        max_length=10,
        verbose_name="Количество человек"
    )
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self) -> str:
        return self.client.first_name + ' ' + self.client.last_name

    def get_absolute_url(self):
        return reverse('create')


