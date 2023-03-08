from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Produto

def product_list(request):
    List = Produto.objects.all()
    return render(request, 'produtos/listagem.html', {'List': List})

def Cadastro(request):
    if request.method == "GET":
        return render(request, 'produtos/cadastro.html')

    abreviacao = request.POST.get('abrevproduto')
    preco = request.POST.get('preco')
    valor_decimal = float(preco.replace(".", "").replace(",", "."))
    descricao = request.POST.get('descricaoProduto')
    imagem = request.FILES.get('imagem')

    produto = Produto.objects.filter(abreviacao=abreviacao).first()
    if produto:
        return render(request, 'produtos/cadastro.html')

    novo_produto = Produto(abreviacao=abreviacao, preco=valor_decimal, descricao=descricao, imagem=imagem)
    novo_produto.save()

    return redirect('home')


