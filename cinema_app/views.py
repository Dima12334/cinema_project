from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login
from .models import *
from .forms import AuthUserForm, RegisterUserForm


class HomeView(ListView):
    model = Film
    template_name = 'cinema_app/index.html'
    context_object_name = 'films'

    def get_context_data(self, **kwargs):
        kwargs['example'] = Film.objects.all().order_by('film_title')
        return super().get_context_data(**kwargs)


class SelectCinemaView(DetailView):
    # model = Cinema
    template_name = 'cinema_app/select_cinema.html'


class BookTicketView(UpdateView):
    # model = Cinema
    template_name = 'cinema_app/book_ticket.html'


class BuyTicketView(UpdateView):
    # model = Cinema
    template_name = 'cinema_app/buy_ticket.html'


class CustomSuccessMessageMixin:

    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


