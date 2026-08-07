from django.urls import path
from . import views

urlpatterns = [
    path('oddlist/', views.odd_list),
    path('oddsum/', views.odd_sum),
]