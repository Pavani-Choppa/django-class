from django.urls import path
import registerapp.views as views

urlpatterns = [
    path('',views.home),
    path('display/',views.display_data)
]