from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Produto

def Listagem(request):
    if request.method == "GET":
        return render(request, 'listagem.html')