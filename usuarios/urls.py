from django.urls import path
from . import views

urlpatterns = [
    path('Cadastro/', views.Cadastro, name='cadastro'),
    path('Login/', views.Login, name='login'),
    path('AlgumaCoisa/', views.AlgumaCoisa, name='AlgumaCoisa'),
    path('VerificarCNPJ/', views.VerificarCNPJ, name='VerificarCNPJ'),
    path('logout/', views.Logout, name='logout'),
    path('LoginInvalid/', views.Login, name='loginInvalid'),
]
