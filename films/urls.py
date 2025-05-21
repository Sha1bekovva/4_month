from django.urls import path
from . import views

urlpatterns = [
    path ('films_list', views.film_list_view, name='films_list'),
    path ('films_list/<int:id>/', views.film_detail_view, name='films_detail'),
]
