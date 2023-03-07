from django.urls import path
from . import views

urlpatterns = [
    path('Sobre/', views.Sobre, name='sobre'),
    path('Home/', views.Home, name='home'),
]

