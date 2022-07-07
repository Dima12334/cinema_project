# Generated by Django 4.0 on 2022-06-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0018_alter_ticket_hall'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buffet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cinema_app/static/cinema_app/images', verbose_name='Фото товару')),
                ('name', models.TextField(verbose_name='Назва товару')),
                ('size', models.TextField(verbose_name='Розмір товару')),
                ('price', models.IntegerField(verbose_name='Ціна товару')),
            ],
            options={
                'verbose_name': 'Буфет',
                'verbose_name_plural': 'Буфет',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='premiere',
            field=models.BooleanField(default=False, verbose_name="Прем'єра"),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='purchased_ticket',
            field=models.IntegerField(verbose_name='Номер квитка'),
        ),
    ]
