from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Tariff(models.Model):
    cost = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    internet = models.IntegerField(default=0)
    messages = models.IntegerField(default=0)


class SupplementedUser(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    telephone_number = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)


class Notification(models.Model):
    receiver = models.ForeignKey(to=SupplementedUser, on_delete=models.CASCADE, related_name="receiver")
    author = models.ForeignKey(to=SupplementedUser, on_delete=models.CASCADE, related_name="author")
    type = models.TextField(default='info')
    event = models.TextField(default='')
    description = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)
