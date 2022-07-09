# Generated by Django 4.0 on 2022-05-13 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaHalls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_count', models.IntegerField()),
                ('ticket_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FilmsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('year', models.IntegerField()),
                ('director', models.CharField(max_length=40)),
                ('rental_period_from', models.DateTimeField()),
                ('rental_period_to', models.DateTimeField()),
                ('language', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=40)),
                ('duration', models.FloatField()),
                ('production', models.CharField(max_length=40)),
                ('scenario', models.TextField()),
                ('main_roles', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SessionsTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_session', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_ticket', models.IntegerField()),
                ('hall_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.cinemahalls')),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_title', models.CharField(max_length=25)),
                ('rating', models.FloatField()),
                ('ticket_price', models.IntegerField()),
                ('story', models.TextField()),
                ('hall_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.cinemahalls')),
                ('id_session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.sessionstime')),
            ],
        ),
        migrations.CreateModel(
            name='Cinemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('film_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.films')),
            ],
        ),
        migrations.AddField(
            model_name='cinemahalls',
            name='id_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.sessionstime'),
        ),
    ]