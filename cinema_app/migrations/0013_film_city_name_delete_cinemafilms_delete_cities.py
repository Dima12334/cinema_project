# Generated by Django 4.0 on 2022-05-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0012_alter_cinemafilms_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='city_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Місто'),
        ),
        migrations.DeleteModel(
            name='CinemaFilms',
        ),
        migrations.DeleteModel(
            name='Cities',
        ),
    ]
