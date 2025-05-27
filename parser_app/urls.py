from django.urls import path
from . import views

urlpatterns = [
    path('parser_form/', views.ParserForm.as_view(), name='parser_form'),
    path('kinov_list/', views.KinovListView.as_view(), name='kinov_list')
]