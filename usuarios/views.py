from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def Cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')

    nomeCompleto = request.POST.get('nomeCompleto')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = User.objects.filter(email=email).first()
    if user:
        return render(request, 'cadastro.html')

    nome = nomeCompleto.split()[0]
    sobrenome = ' '.join(nomeCompleto.split()[1:])
    user = User.objects.create_user(
        username=email, password=senha, email=email)

    user.first_name = nome
    user.last_name = sobrenome

    user.save()

    return render(request, 'login.html')


def Login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    email = request.POST.get('email')
    senha = request.POST.get('senha')
    user = None
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # email não existe
        return HttpResponse('Usuário ou senha inválidos')

    if user.check_password(senha):
        # senha válida, autenticar usuário
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return HttpResponse('Deu certo!')

    return HttpResponse('Usuário ou senha inválidos')


@login_required
def AlgumaCoisa(request):
    return HttpResponse('Plataforma')


def Logout(request):
    logout(request)
    return redirect('login')
