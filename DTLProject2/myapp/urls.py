
from django.urls import path
from . import views
urlpatterns = [
    path('blog/',views.index,name='home'),
    path('display/',views.display,name='display'),
    path('about/',views.about,name='about'),
]