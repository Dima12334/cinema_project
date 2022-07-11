from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search', views.Search.as_view(), name='search'),
    path('<slug:slug>', views.FilmDetailView.as_view(), name='film-details'),
    path('review/<int:pk>', views.AddReview.as_view(), name='add-review'),
    path('<int:pk_rev>/<int:pk_film>/like/', views.AddLike.as_view(), name='like'),
    path('<int:pk_rev>/<int:pk_film>/dislike/', views.AddDislike.as_view(), name='dislike'),
    path('ticket/<int:pk>/<int:hall>', views.BuyBookTicketView.as_view(), name='buybook-ticket'),

]
