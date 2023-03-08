from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Produto

def product_list(request):
    List = Produto.objects.all()
    return render(request, 'produtos/listagem.html', {'List': List})

def Cadastro(request):
    if request.method == "GET":
        return render(request, 'produtos/cadastro.html')
