# Generated by Django 4.0 on 2022-05-24 09:13

from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.detail
import django.views.generic.list


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0013_film_city_name_delete_cinemafilms_delete_cities'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmDetails',
            fields=[
                ('film_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cinema_app.film')),
            ],
            bases=('cinema_app.film', django.views.generic.detail.DetailView),
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
        migrations.RemoveField(
            model_name='rating',
            name='film',
        ),
        migrations.AddField(
            model_name='film',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Вік'),
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.CharField(max_length=40, null=True, verbose_name='Режисер'),
        ),
        migrations.AddField(
            model_name='film',
            name='duration',
            field=models.FloatField(null=True, verbose_name='Тривалість'),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.CharField(max_length=50, null=True, verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.CharField(max_length=50, null=True, verbose_name='Мова'),
        ),
        migrations.AddField(
            model_name='film',
            name='main_roles',
            field=models.TextField(null=True, verbose_name='У головних ролях'),
        ),
        migrations.AddField(
            model_name='film',
            name='production',
            field=models.CharField(max_length=100, null=True, verbose_name='Виробництво'),
        ),
        migrations.AddField(
            model_name='film',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.rating', verbose_name='Рейтинг фільму'),
        ),
        migrations.AddField(
            model_name='film',
            name='rental_period_from',
            field=models.DateField(null=True, verbose_name='Прокат від'),
        ),
        migrations.AddField(
            model_name='film',
            name='rental_period_to',
            field=models.DateField(null=True, verbose_name='Прокат до'),
        ),
        migrations.AddField(
            model_name='film',
            name='year',
            field=models.IntegerField(null=True, verbose_name='Рік'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating_value',
            field=models.IntegerField(null=True, verbose_name='Кількість зірок'),
        ),
        migrations.AlterField(
            model_name='review',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.film', verbose_name='Назва фільму'),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('filmdetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cinema_app.filmdetails')),
            ],
            bases=('cinema_app.filmdetails', django.views.generic.list.ListView),
        ),
        migrations.DeleteModel(
            name='FilmDetail',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
