from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, View
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login
from django.db.models import Q
from .models import *


class HomeView(ListView):
    model = Film
    template_name = 'cinema_app/index.html'
    context_object_name = 'films'

    def get_context_data(self, **kwargs):
        kwargs['example'] = Film.objects.all().order_by('film_title')
        return super().get_context_data(**kwargs)


class Search(ListView):

    def get_queryset(self):
        return Film.objects.filter(city_name__icontains=self.request.GET.get("q"))

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["q"] = self.request.GET.get("q")
    #     return context


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


