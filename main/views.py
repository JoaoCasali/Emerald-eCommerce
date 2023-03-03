from django.http import HttpResponse
from django.shortcuts import render, redirect

def Home(request):
    return render(request, 'home.html')

def Sobre(request):
    return render(request, 'sobre.html')
