from django.db import models

# Create your models here.


class Tariff(models.Model):
    cost = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    internet = models.IntegerField(default=0)
    messages = models.IntegerField(default=0)
