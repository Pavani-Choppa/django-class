from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_method),
    path('update/', views.update_method),
    path('pop/', views.pop_method),
    path('remove/', views.remove_method),
]