# Generated by Django 4.0 on 2022-05-18 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0009_alter_film_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.filmdetail', verbose_name='Назва фільму'),
        ),
    ]
