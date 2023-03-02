from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Cliente

def Cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')

    nomeCompleto = request.POST.get('nomeCompleto')
    cpf_cnpj = request.POST.get('cpf_cnpj')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = Cliente.objects.filter(email=email).first()
    if user:
        return render(request, 'cadastro.html')

    cpf_cnpj = ' '.join([int(digit) for digit in cpf_cnpj if digit.isdigit()])

    nome = nomeCompleto.split()[0]
    sobrenome = ' '.join(nomeCompleto.split()[1:])
    user = Cliente.objects.create_user(
        username=email, password=senha, email=email, cpf_cnpj = cpf_cnpj)

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
        user = Cliente.objects.get(email=email)
    except Cliente.DoesNotExist:
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
