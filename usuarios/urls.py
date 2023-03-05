from django.urls import path
from . import views

urlpatterns = [
    path('Cadastro/', views.Cadastro, name='cadastro'),
    path('Login/', views.Login, name='login'),
    path('AlgumaCoisa/', views.AlgumaCoisa, name='AlgumaCoisa'),
    path('Logout/', views.Logout, name='logout'),
]
