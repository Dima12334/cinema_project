from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('', views.Store.as_view(), name='store'),
    path('search', views.Search.as_view(), name='search'),
    path('<slug:slug>', views.FilmDetailView.as_view(), name='film-details'),
    path('review/<int:pk>', views.AddReview.as_view(), name='add-review'),
    path('ticket/<int:pk>/<int:hall>', views.BuyTicketView.as_view(), name='buy-ticket'),
    path('ticket/<int:pk>/<int:hall>', views.BookTicketView.as_view(), name='book-ticket'),

]
