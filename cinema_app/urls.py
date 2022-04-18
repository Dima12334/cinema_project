from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('select_cinema', views.SelectCinemaView.as_view(), name='select-cinema'),
    path('book_ticket', views.BookTicketView.as_view(), name='book-ticket'),
    path('buy_ticket', views.BuyTicketView.as_view(), name='buy-ticket'),
    path('login', views.LoginPage.as_view(), name='login-page'),
    path('register', views.RegisterPage.as_view(), name='register-page'),
    path('logout', views.LogOutPage.as_view(), name='logout-page'),

]