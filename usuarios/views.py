from django.http import HttpResponse, JsonResponse
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

    cpfCnpjLimpo = [str(digit) for digit in cpf_cnpj if digit.isdigit()]

    cpf_cnpj = ''.join(cpfCnpjLimpo)

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
        current = request.build_absolute_uri('/')
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
            return redirect('home')


    return HttpResponse('Usuário ou senha inválidos')


@login_required
def AlgumaCoisa(request):
    return HttpResponse('Plataforma')


def Logout(request):
    logout(request)
    return redirect('login')


def VerificarCNPJ(request):
    cnpj = request.GET.get('cnpj')

    cnpj_limpo = [int(char) for char in cnpj if char.isdigit()]

    # considera-se erro CNPJ's formados por uma sequencia de numeros iguais
    if (cnpj_limpo == "00000000000000" or cnpj_limpo == "11111111111111" or cnpj_limpo == "22222222222222" or
        cnpj_limpo == "33333333333333" or cnpj_limpo == "44444444444444" or cnpj_limpo == "55555555555555" or
        cnpj_limpo == "66666666666666" or cnpj_limpo == "77777777777777" or cnpj_limpo == "88888888888888" or
        cnpj_limpo == "99999999999999" or len(cnpj_limpo) != 14):
       
       return JsonResponse({"Resposta": False})

    try:
        sm = 0
        peso = 2
        for i in range(11, -1, -1):
            num = int(cnpj[i])
            sm += num * peso
            peso += 1
            if peso == 10:
                peso = 2

        r = sm % 11
        if r == 0 or r == 1:
            dig13 = '0'
        else:
            dig13 = chr(11 - r + 48)

        sm = 0
        peso = 2
        for i in range(12, -1, -1):
            num = int(cnpj[i])
            sm += num * peso
            peso += 1
            if peso == 10:
                peso = 2

        r = sm % 11
        if r == 0 or r == 1:
            dig14 = '0'
        else:
            dig14 = chr(11 - r + 48)

        if dig13 == cnpj[12] and dig14 == cnpj[13]:
            return JsonResponse({"Resposta": True})

        else:
            return JsonResponse({"Resposta": False})
    except ValueError:
        return JsonResponse({"Resposta": False})




