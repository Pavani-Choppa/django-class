from django.urls import path
from . import views

urlpatterns = [
    path('evenlist/', views.even_list),
    path('evensum/', views.even_sum),
]