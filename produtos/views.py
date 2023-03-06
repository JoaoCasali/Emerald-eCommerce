from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Produto

def product_list(request):
    List = Produto.objects.all()
    return render(request, 'listagem.html', {'List': List})

# def product_list(request):
#     numbers = [1, 2, 3, 4, 5]
#     context = {'numbers': numbers}
#     return render(request, 'listagem.html', context)
def Cadastro(request):
    if request.method == "GET":
        return render(request, 'produtos/cadastro.html')
