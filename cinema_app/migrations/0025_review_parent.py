# Generated by Django 4.0 on 2022-07-08 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0024_alter_film_director_alter_film_film_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema_app.review', verbose_name='Батько'),
        ),
    ]
