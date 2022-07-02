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


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ['name', 'email']


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['film_title', 'rating', 'hall', 'session', 'get_image', 'city_name', 'age',
                    'director', 'rental_period_from', 'rental_period_to', 'premiere']
    list_display_links = ['film_title', 'rating', 'hall', 'session', 'get_image', 'city_name', 'age',
                          'director', 'rental_period_from', 'rental_period_to']
    ordering = ['film_title']
    readonly_fields = ['get_image']
    list_per_page = 10
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')
    get_image.short_description = 'Постер'


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


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['rating_value']
    list_display_links = ['rating_value']
    ordering = ['rating_value']
    list_per_page = 7


@admin.register(Buffet)
class BuffetAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'name', 'size', 'price']
    list_display_links = ['name', 'size', 'price']
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Товар'


admin.site.site_header = 'Управление cinema'
admin.site.index_title = 'Админка сайта'
