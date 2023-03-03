from django.urls import path
from . import views

urlpatterns = [
    path('sobre/', views.Sobre, name='sobre'),
    path('home/', views.Sobre, name='sobre'),
]
