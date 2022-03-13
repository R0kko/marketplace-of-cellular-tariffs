from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import date
from django.utils import timezone


# Create your models here.


class Operator(models.Model):
    name = models.CharField(default='Название оператора', max_length=256)
    website_link = models.CharField(default='/', max_length=256)
    icon = models.ImageField(upload_to='operator_icons/', default='')


class Tariff(models.Model):
    cost = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    internet = models.IntegerField(default=0)
    messages = models.IntegerField(default=0)
    name = models.CharField(default='Название тарифа', max_length=256)
    operator = models.ForeignKey(Operator, null=True, on_delete=models.CASCADE)
    general_information = models.TextField(default='Общая информация о тарифе')


class SupplementedUser(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    patronymic = models.TextField(default='', max_length=255)
    telephone_number = models.TextField(default='', max_length=14)
    date_of_birth = models.DateField(default=date.today)


class Notification(models.Model):
    receiver = models.ForeignKey(to=SupplementedUser, on_delete=models.CASCADE, related_name="receiver")
    author = models.ForeignKey(to=SupplementedUser, on_delete=models.CASCADE, related_name="author")
    type = models.TextField(default='info')
    event = models.TextField(default='')
    description = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)
# daun zachem dobavil etu kakashku