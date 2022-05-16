from django.db import models
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User


class TimeSessions(models.Model):
    time_session = models.TimeField(verbose_name='Сеанс')

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеанси'

    def __str__(self):
        return f'{self.time_session}'


class CinemaHalls(models.Model):
    number_hall = models.IntegerField(verbose_name='Номер кінозалу')
    row_count = models.IntegerField(verbose_name='Кількість рядів')
    ticket_count = models.IntegerField(verbose_name='Кількість квитків')
    # session = models.ForeignKey(TimeSessions, on_delete=models.CASCADE, verbose_name='Сеанс', blank=True,
    #                            null=True)  # id_session

    class Meta:
        verbose_name = 'Кінозал'
        verbose_name_plural = 'Кінозали'

    def __str__(self):
        return f'{self.number_hall} кінозал'


class Films(models.Model):
    film_title = models.CharField(max_length=25, verbose_name='Назва фільму')
    rating = models.FloatField(verbose_name='Рейтинг фільму')
    ticket_price = models.IntegerField(verbose_name='Ціна квитка')
    hall = models.ForeignKey(CinemaHalls, on_delete=models.CASCADE, verbose_name='Зал', blank=True,
                             null=True)  # hall_id
    story = models.TextField(verbose_name='Сюжет')
    session = models.ForeignKey(TimeSessions, on_delete=models.CASCADE, verbose_name='Сеанс', blank=True,
                                null=True)  # id_session

    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'

    def __str__(self):
        return f'{self.film_title}'


class FilmDetails(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE, verbose_name='Назва фільму', blank=True,
                             null=True)  # film_id
    age = models.IntegerField(verbose_name='Вік')
    year = models.IntegerField(verbose_name='Рік')
    director = models.CharField(max_length=40, verbose_name='Режисер')
    rental_period_from = models.DateField(auto_now=False, verbose_name='Прокат від')  # verbose_name='Прокат від'
    rental_period_to = models.DateField(auto_now=False, verbose_name='Прокат до')  # verbose_name='Прокат до'
    language = models.CharField(max_length=40, verbose_name='Мова')
    genre = models.CharField(max_length=40, verbose_name='Жанр')
    duration = models.FloatField(verbose_name='Тривалість')
    production = models.CharField(max_length=40, verbose_name='Виробництво')
    scenario = models.TextField(verbose_name='Сценарій')
    main_roles = models.TextField(verbose_name='У головних ролях')

    class Meta:
        verbose_name = 'Деталі фільму'
        verbose_name_plural = 'Деталі фільмів'

    def __str__(self):
        return f'{self.age} {self.year} {self.director} {self.rental_period_from} {self.rental_period_to} \
        {self.language} {self.genre} {self.duration} {self.production} {self.scenario} {self.main_roles}'


class Cinemas(models.Model):
    city = models.CharField(max_length=25, verbose_name='Місто')
    film = models.ForeignKey(Films, on_delete=models.CASCADE, verbose_name='Назва фільму', blank=True,
                             null=True)  # film_id

    class Meta:
        verbose_name = 'Кінотеатр'
        verbose_name_plural = 'Кінотеатри'

    def __str__(self):
        return f'{self.city} {self.film}'


class Tickets(models.Model):
    hall = models.OneToOneField(CinemaHalls, on_delete=models.CASCADE, verbose_name='Зал', blank=True,
                                null=True)  # hall_id
    purchased_ticket = models.IntegerField(verbose_name='Продані квитки')

    class Meta:
        verbose_name = 'Проданий квиток'
        verbose_name_plural = 'Продані квитки'

    def __str__(self):
        return f'{self.hall} {self.purchased_ticket}'
