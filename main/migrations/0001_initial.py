# Generated by Django 3.1.6 on 2022-03-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(default=0)),
                ('internet', models.IntegerField(default=0)),
                ('messages', models.IntegerField(default=0)),
            ],
        ),
    ]
