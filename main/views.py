from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')

def PageNotFound(request, exception):
    return render(request, 'notFound.css')