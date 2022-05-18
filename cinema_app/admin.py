from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(TimeSession)
class TimeSessionAdmin(admin.ModelAdmin):
    list_display = ['time_session']
    list_display_links = ['time_session']
    ordering = ['time_session']
    list_per_page = 7


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ['number_hall', 'row_count', 'ticket_count']
    list_display_links = ['number_hall', 'row_count', 'ticket_count']
    ordering = ['id']
    list_per_page = 7


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['film_title', 'ticket_price', 'hall', 'story', 'session']
    list_display_links = ['film_title', 'ticket_price', 'hall', 'story', 'session']
    ordering = ['film_title']
    list_per_page = 7


@admin.register(FilmDetail)
class FilmDetailAdmin(admin.ModelAdmin):
    list_display = ['film', 'age', 'year', 'director', 'rental_period_from', 'rental_period_to', 'language', 'genre',
                    'duration', 'production', 'scenario', 'main_roles', 'rating']
    list_display_links = ['film', 'age', 'year', 'director', 'rental_period_from', 'rental_period_to', 'language',
                          'genre', 'duration', 'production', 'scenario', 'main_roles', 'rating']
    ordering = ['genre']
    list_per_page = 7


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['city', 'film']
    list_display_links = ['city', 'film']
    ordering = ['city']
    list_per_page = 7


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['hall']
    list_display_links = ['hall']
    ordering = ['hall']
    list_per_page = 7


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'film']
    ordering = ['film']
    list_per_page = 7


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ['value']
    list_display_links = ['value']
    ordering = ['value']
    list_per_page = 7


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['film', 'rating_value']
    list_display_links = ['film', 'rating_value']
    ordering = ['film']
    list_per_page = 7
