from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search', views.Search.as_view(), name='search'),
    path('book_ticket', views.BookTicketView.as_view(), name='book-ticket'),
    path('buy_ticket', views.BuyTicketView.as_view(), name='buy-ticket'),

]
