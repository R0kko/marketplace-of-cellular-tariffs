# Generated by Django 4.0.2 on 2022-03-13 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20220313_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='SupplementedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.TextField(default='', max_length=255)),
                ('telephone_number', models.TextField(default='', max_length=14)),
                ('date_of_birth', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(default='info')),
                ('event', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='main.supplementeduser')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='main.supplementeduser')),
            ],
        ),
    ]
