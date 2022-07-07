# Generated by Django 4.0 on 2022-05-19 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0010_alter_review_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaFilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Кінотеатр',
                'verbose_name_plural': 'Кінотеатри',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, verbose_name='Місто')),
            ],
            options={
                'verbose_name': 'Місто',
                'verbose_name_plural': 'Міста',
            },
        ),
        migrations.AlterField(
            model_name='film',
            name='film_title',
            field=models.CharField(max_length=50, verbose_name='Назва фільму'),
        ),
        migrations.AlterField(
            model_name='filmdetail',
            name='genre',
            field=models.CharField(max_length=50, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='filmdetail',
            name='language',
            field=models.CharField(max_length=50, verbose_name='Мова'),
        ),
        migrations.AlterField(
            model_name='filmdetail',
            name='production',
            field=models.CharField(max_length=100, verbose_name='Виробництво'),
        ),
        migrations.DeleteModel(
            name='Cinema',
        ),
        migrations.AddField(
            model_name='cinemafilms',
            name='city',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.cities', verbose_name='Місто'),
        ),
        migrations.AddField(
            model_name='cinemafilms',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.film', verbose_name='Назва фільму'),
        ),
    ]
