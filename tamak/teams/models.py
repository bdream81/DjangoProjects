from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Team(models.Model):
    EDUCATIONS = (
        ('Bachelor', 'Бакалавр'),
        ('College', 'Техникум или Коледж'),
        ('Self-Educated', 'Самоучка')
    )

    POSITIONS = (
        ('Генеральный Директор', 'Генеральный Директор'),
        ('Шеф Повар', 'Шеф Повар'),
        ('Повар', 'Повар'),
        ('Стажёр', 'Стажёр')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    positions = models.CharField(
        choices=EDUCATIONS,
        max_length=100, verbose_name="Должность")
    educations = models.CharField(
        choices=POSITIONS,
        max_length=100, verbose_name="Образование")
    experience = models.IntegerField(verbose_name="Реальный стаж")
    companies = models.CharField(max_length=256, verbose_name="История")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.user.username

    def get_absolute_url(self):
        return reverse('team_view')
   


