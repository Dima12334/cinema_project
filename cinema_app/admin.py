from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(TimeSessions)
class TimeSessionsAdmin(admin.ModelAdmin):
    list_display = ['time_session']
    list_display_links = ['time_session']
    ordering = ['time_session']
    list_per_page = 7


@admin.register(CinemaHalls)
class CinemaHallsAdmin(admin.ModelAdmin):
    list_display = ['row_count', 'ticket_count', 'session']
    list_display_links = ['row_count', 'ticket_count', 'session']
    ordering = ['session']
    list_per_page = 7


@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    list_display = ['film_title', 'rating', 'ticket_price', 'hall', 'story', 'session']
    list_display_links = ['film_title', 'rating', 'ticket_price', 'hall', 'story', 'session']
    ordering = ['film_title']
    list_per_page = 7


@admin.register(FilmDetails)
class FilmDetailsAdmin(admin.ModelAdmin):
    list_display = ['age', 'year', 'director', 'rental_period_from', 'rental_period_to', 'language', 'genre',
                    'duration', 'production', 'scenario', 'main_roles']
    list_display_links = ['age', 'year', 'director', 'rental_period_from', 'rental_period_to', 'language', 'genre',
                          'duration', 'production', 'scenario', 'main_roles']
    ordering = ['genre']
    list_per_page = 7


@admin.register(Cinemas)
class CinemasAdmin(admin.ModelAdmin):
    list_display = ['city', 'film']
    list_display_links = ['city', 'film']
    ordering = ['city']
    list_per_page = 7


@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ['hall']
    list_display_links = ['hall']
    ordering = ['hall']
    list_per_page = 7
