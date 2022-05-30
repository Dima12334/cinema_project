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
from django.db.models import Q
from .forms import BuyTicketForm, ReviewForm
from .models import *


# class CustomSuccessMessageMixin:
#
#     @property
#     def success_msg(self):
#         return False
#
#     def form_valid(self, form):
#         messages.success(self.request, self.success_msg)
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return '%s?id=%s' % (self.success_url, self.object.id)


class HomeView(ListView):
    model = Film
    template_name = 'cinema_app/index.html'
    context_object_name = 'films'

    def get_context_data(self, **kwargs):
        kwargs['example'] = Film.objects.all().order_by('film_title')
        return super().get_context_data(**kwargs)


class FilmDetailView(DetailView):
    model = Film
    slug_field = "url"


class Search(ListView):

    def get_queryset(self):
        return Film.objects.filter(city_name__icontains=self.request.GET.get("q"))

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
        return redirect(film.get_absolute_url())


class BuyTicketView(View):

    def post(self, request, pk, hall):
        form = BuyTicketForm(request.POST)
        film = Film.objects.get(id=pk)
        hall = CinemaHall.objects.get(number_hall=hall)
        if form.is_valid():
            form = form.save(commit=False)
            form.film = film
            form.hall = hall
            form.save()
        return redirect(film.get_absolute_url())


class BookTicketView(UpdateView):
    # model = Cinema
    template_name = 'cinema_app/book_ticket.html'



