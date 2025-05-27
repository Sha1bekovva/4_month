from django.urls import path
from . import views

urlpatterns = [
    path ('films_list/', views.FilmListView.as_view(), name='films_list'),
    path ('films_list/<int:id>/', views.FilmDetailView.as_view(), name='films_detail'),
    path ('films_list/<int:id>/delete/', views.DeleteFilmView.as_view(), name='delete_film'),
    path ('films_list/<int:id>/update/', views.UpdateFilmView.as_view(), name='update_film'),
    path ('create_film/', views.CreateFilmView.as_view(), name='create_film'),
    path('search/', views.SearchFilmView.as_view(), name='search'),
]
