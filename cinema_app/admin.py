from django.contrib import admin
from django.utils.safestring import mark_safe

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
    list_display = ['film_title', 'ticket_price', 'hall', 'story', 'session', 'get_image']
    list_display_links = ['film_title', 'ticket_price', 'hall', 'story', 'session']
    ordering = ['film_title']
    readonly_fields = ['get_image']
    list_per_page = 7

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')

    get_image.short_description = 'Постер'


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ['name', 'email']


@admin.register(FilmDetail)
class FilmDetailAdmin(admin.ModelAdmin):
    list_display = ['film', 'age', 'year', 'director', 'rental_period_from', 'rental_period_to', 'language', 'genre',
                    'duration', 'production', 'scenario', 'main_roles', 'rating']
    list_display_links = ['film', 'age', 'year', 'director', 'rental_period_from', 'rental_period_to', 'language',
                          'genre', 'duration', 'production', 'scenario', 'main_roles', 'rating']
    ordering = ['genre']
    list_per_page = 7
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['city', 'film']
    list_display_links = ['city', 'film']
    ordering = ['city']
    list_per_page = 7


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['hall', 'purchased_ticket']
    list_display_links = ['hall', 'purchased_ticket']
    ordering = ['hall']
    readonly_fields = ['purchased_ticket']
    list_per_page = 7


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text', 'film']
    ordering = ['film']
    readonly_fields = ['name', 'email']
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


admin.site.site_header = 'Управление cinema'
admin.site.index_title = 'Админка сайта'
