from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, View
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.db.models import Q
from .forms import *
from .models import *
from django.core.mail import send_mail


# def post_message(request, pk):
#
#     form = PostMessageForm()
#     if request.method == 'POST':
#         form = PostMessageForm(request.POST)
#         film = Film.objects.get(id=pk)
#         if form.is_valid():
#             form.email = settings.EMAIL_HOST_USER
#             subject = 'Code Band'
#             message = 'Sending Email through Gmail'
#             recipient = form.email
#             send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
#             messages.success(request, 'Success!')
#     return redirect(film.get_absolute_url())


class StoreSlider:

    def get_buffet(self):
        return Buffet.objects.all()

    def get_slider(self):
        return Film.objects.filter(premiere=False, city_name='Харків')


class HomeView(StoreSlider, ListView):
    model = Film
    template_name = 'cinema_app/index.html'
    context_object_name = 'films'

    def get_context_data(self, **kwargs):
        kwargs['films'] = Film.objects.filter(premiere=True).order_by('rental_period_from')
        return super().get_context_data(**kwargs)


class FilmDetailView(DetailView):
    model = Film
    slug_field = "url"


class Search(ListView):

    def get_queryset(self):
        return Film.objects.filter(city_name__icontains=self.request.GET.get("q"), premiere=False).order_by('session')

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["q"] = self.request.GET.get("q")
    #     return context


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        film = Film.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.film = film
            form.name = self.request.user.username
            form.email = self.request.user.email
            form.save()
            messages.success(request, 'Ваш відгук залишено!')
        return redirect(film.get_absolute_url())


class BuyBookTicketView(View):

    def post(self, request, pk, hall):
        form = BuyBookTicketForm(request.POST)
        film = Film.objects.get(id=pk)
        hall = CinemaHall.objects.get(number_hall=hall)
        if form.is_valid():
            form = form.save(commit=False)
            form.film = film
            form.hall = hall
            form.save()
            messages.success(request, 'Квиток списано!')
        return redirect(film.get_absolute_url())  # post_message(request, pk)
