from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.Cadastro, name='cadastro'),
    path('login/', views.Login, name='login'),
    path('AlgumaCoisa/', views.AlgumaCoisa, name='AlgumaCoisa'),
    path('logout/', views.Logout, name='logout'),
]
