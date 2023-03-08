from django.shortcuts import render

def Home(request):
    return render(request, 'main/home.html')

def Sobre(request):
    return render(request, 'main/sobre.html')

def PageNotFound(request, exception = None):
    return render(request, 'main/notFound.html')