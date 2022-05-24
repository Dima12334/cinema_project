from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class TimeSession(models.Model):
    time_session = models.TimeField(verbose_name='Сеанс')

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеанси'

    def __str__(self):
        return f'{self.time_session}'


class CinemaHall(models.Model):
    number_hall = models.IntegerField(verbose_name='Номер кінозалу')
    row_count = models.IntegerField(verbose_name='Кількість рядів')
    ticket_count = models.IntegerField(verbose_name='Кількість квитків')

    # session = models.ForeignKey(TimeSessions, on_delete=models.CASCADE, verbose_name='Сеанс', blank=True,
    #                            null=True)  # time_session

    class Meta:
        verbose_name = 'Кінозал'
        verbose_name_plural = 'Кінозали'

    def __str__(self):
        return f'{self.number_hall}'


# class RatingStar(models.Model):
#     value = models.IntegerField(verbose_name='Рейтинг фільму')
#
#     class Meta:
#         verbose_name = 'Зірка'
#         verbose_name_plural = 'Зірки'
#
#     def __str__(self):
#         return f'{self.value}'


class Rating(models.Model):
    rating_value = models.IntegerField(verbose_name='Кількість зірок', null=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return f'{self.rating_value}'


class Film(models.Model):
    film_title = models.CharField(max_length=50, verbose_name='Назва фільму')
    ticket_price = models.IntegerField(verbose_name='Ціна квитка')
    hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, verbose_name='Зал', blank=True,
                             null=True)  # number_hall
    story = models.TextField(verbose_name='Сюжет')
    session = models.ForeignKey(TimeSession, on_delete=models.CASCADE, verbose_name='Сеанс', blank=True,
                                null=True)  # time_session
    poster = models.ImageField(upload_to='cinema_app/static/cinema_app/images')
    city_name = models.CharField(max_length=100, verbose_name='Місто', null=True)
    age = models.IntegerField(verbose_name='Вік', null=True)
    year = models.IntegerField(verbose_name='Рік', null=True)
    director = models.CharField(max_length=40, verbose_name='Режисер', null=True)
    rental_period_from = models.DateField(auto_now=False, verbose_name='Прокат від', null=True)
    rental_period_to = models.DateField(auto_now=False, verbose_name='Прокат до', null=True)
    language = models.CharField(max_length=50, verbose_name='Мова', null=True)
    genre = models.CharField(max_length=50, verbose_name='Жанр', null=True)
    duration = models.FloatField(verbose_name='Тривалість', null=True)
    production = models.CharField(max_length=100, verbose_name='Виробництво', null=True)
    main_roles = models.TextField(verbose_name='У головних ролях', null=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, verbose_name='Рейтинг фільму', blank=True,
                               null=True)  # rating_value
    url = models.SlugField(max_length=130, unique=True, null=True)

    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'

    def __str__(self):
        return f'{self.film_title}'

    def get_absolute_url(self):
        return reverse("film-details", kwargs={"slug": self.url})


# class FilmDetail(models.Model):
#     film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Назва фільму', blank=True,
#                              null=True)  # film_title
#     age = models.IntegerField(verbose_name='Вік')
#     year = models.IntegerField(verbose_name='Рік')
#     director = models.CharField(max_length=40, verbose_name='Режисер')
#     rental_period_from = models.DateField(auto_now=False, verbose_name='Прокат від')
#     rental_period_to = models.DateField(auto_now=False, verbose_name='Прокат до')
#     language = models.CharField(max_length=50, verbose_name='Мова')
#     genre = models.CharField(max_length=50, verbose_name='Жанр')
#     duration = models.FloatField(verbose_name='Тривалість')
#     production = models.CharField(max_length=100, verbose_name='Виробництво')
#     scenario = models.TextField(verbose_name='Сценарій')
#     main_roles = models.TextField(verbose_name='У головних ролях')
#     rating = models.ForeignKey(Rating, on_delete=models.CASCADE, verbose_name='Рейтинг фільму', blank=True,
#                                null=True)  # rating_value
#
#     class Meta:
#         verbose_name = 'Деталі фільму'
#         verbose_name_plural = 'Деталі фільмів'
#
#     def __str__(self):
#         return f'{self.age} {self.year} {self.director} {self.rental_period_from} {self.rental_period_to} \
#         {self.language} {self.genre} {self.duration} {self.production} {self.scenario} {self.main_roles}'


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Назва фільму', blank=True,
                             null=True)  # film_title

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return f'{self.film} -- {self.text}'


# class Cities(models.Model):
#     city_name = models.CharField(max_length=100, verbose_name='Місто')
#
#     class Meta:
#         verbose_name = 'Місто'
#         verbose_name_plural = 'Міста'
#
#     def __str__(self):
#         return f'{self.city_name}'
#
#
# class CinemaFilms(models.Model):
#     city = models.ForeignKey(Cities, on_delete=models.CASCADE, verbose_name='Місто', blank=True,
#                              null=True)  # city_name
#     film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Назва фільму', blank=True,
#                              null=True)  # film_title
#
#     class Meta:
#         verbose_name = 'Кінотеатр'
#         verbose_name_plural = 'Кінотеатри'
#
#     def __str__(self):
#         return f'{self.city} -- {self.film}'


class Ticket(models.Model):
    hall = models.OneToOneField(CinemaHall, on_delete=models.CASCADE, verbose_name='Зал', blank=True,
                                null=True)  # number_hall
    purchased_ticket = models.IntegerField(verbose_name='Продані квитки')

    class Meta:
        verbose_name = 'Проданий квиток'
        verbose_name_plural = 'Продані квитки'

    def __str__(self):
        return f'{self.hall} {self.purchased_ticket}'
