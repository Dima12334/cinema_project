from django.db import models
from django.urls import reverse


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

    class Meta:
        verbose_name = 'Кінозал'
        verbose_name_plural = 'Кінозали'

    def __str__(self):
        return f'{self.number_hall}'


class Rating(models.Model):
    rating_value = models.IntegerField(verbose_name='Кількість зірок', null=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return f'{self.rating_value}'


class Film(models.Model):
    film_title = models.CharField(max_length=200, verbose_name='Назва фільму')
    ticket_price = models.IntegerField(verbose_name='Ціна квитка')
    hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, verbose_name='Зал', blank=True,
                             null=True)  # number_hall
    story = models.TextField(verbose_name='Сюжет')
    session = models.ForeignKey(TimeSession, on_delete=models.CASCADE, verbose_name='Сеанс', blank=True,
                                null=True)  # time_session
    poster = models.ImageField(verbose_name="Постер", upload_to='cinema_app/static/cinema_app/images')
    city_name = models.CharField(max_length=100, verbose_name='Місто', null=True)
    age = models.IntegerField(verbose_name='Вік', null=True)
    year = models.IntegerField(verbose_name='Рік', null=True)
    director = models.CharField(max_length=100, verbose_name='Режисер', null=True)
    rental_period_from = models.DateField(auto_now=False, verbose_name='Прокат від', null=True)
    rental_period_to = models.DateField(auto_now=False, verbose_name='Прокат до', null=True)
    language = models.CharField(max_length=100, verbose_name='Мова', null=True)
    genre = models.CharField(max_length=100, verbose_name='Жанр', null=True)
    duration = models.FloatField(verbose_name='Тривалість', null=True)
    production = models.CharField(max_length=100, verbose_name='Виробництво', null=True)
    main_roles = models.TextField(verbose_name='У головних ролях', null=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, verbose_name='Рейтинг фільму', blank=True,
                               null=True)  # rating_value
    url = models.SlugField(max_length=130, unique=True, null=True)
    premiere = models.BooleanField("Прем'єра", default=False)

    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'

    def __str__(self):
        return f'{self.film_title}'

    def get_absolute_url(self):
        return reverse("film-details", kwargs={"slug": self.url})

    def get_review(self):
        return self.review_set.filter(parent__isnull=True)


class Review(models.Model):
    email = models.EmailField(verbose_name='Email автора')
    name = models.CharField(max_length=100, verbose_name="Ім'я автора")
    text = models.TextField(max_length=5000, verbose_name='Текст відгука')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Назва фільму', blank=True,
                             null=True)  # film_title
    parent = models.ForeignKey('self', verbose_name="Батько", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return f'{self.film} -- {self.text}'


class Ticket(models.Model):
    purchased_ticket = models.IntegerField(verbose_name='Номер квитка')
    hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, verbose_name='Номер залу', blank=True,
                             null=True)  # number_hall
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Назва фільму', blank=True,
                             null=True)  # film_title

    class Meta:
        verbose_name = 'Проданий квиток'
        verbose_name_plural = 'Продані квитки'

    def __str__(self):
        return f'{self.purchased_ticket}'


class Buffet(models.Model):
    image = models.ImageField(verbose_name="Фото товару", upload_to='cinema_app/static/cinema_app/images/buffet',
                              null=True)
    name = models.TextField(verbose_name="Назва товару")
    size = models.TextField(verbose_name="Розмір товару")
    price = models.IntegerField(verbose_name="Ціна товару")

    class Meta:
        verbose_name = 'Буфет'
        verbose_name_plural = 'Буфет'

