from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')

def Sobre(request):
    return render(request, 'sobre.html')

def PageNotFound(request, ex):
    return render(request, 'notFound.html')