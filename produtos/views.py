from django.shortcuts import render

def Cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
