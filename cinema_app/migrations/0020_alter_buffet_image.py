# Generated by Django 4.0 on 2022-06-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0019_buffet_film_premiere_alter_ticket_purchased_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buffet',
            name='image',
            field=models.ImageField(upload_to='static/images/buffet', verbose_name='Фото товару'),
        ),
    ]
