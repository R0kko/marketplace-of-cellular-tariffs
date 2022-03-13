from django.db import models

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
