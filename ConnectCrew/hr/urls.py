from django.urls import path
from hr import views
urlpatterns = [
    path('', views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    # path("viewemployees/", viewemployees, name="viewemployees"),

]