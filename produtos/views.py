from django.shortcuts import render

def CadastroProduto(request):
    if request.method == "GET":
        return render(request, 'cadastro1.html')
