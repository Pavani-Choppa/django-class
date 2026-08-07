from django.urls import path
from . import views

urlpatterns = [
    path('append/', views.append_method),
    path('extend/', views.extend_method),
    path('pop/', views.pop_method),
    path('remove/', views.remove_method),
]