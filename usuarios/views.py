from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html' , {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status})

def valida_cadastro(request):

    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, 
                          senha = senha, 
                          email = email)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')  
    except:
       return redirect('/auth/cadastro/?status=4')
    
def valida_login(request):

    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    #verificação no banco de dados para bater usuario e senha
    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    # igual a zero ele não existe
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    # maior que 0 ele existe
    elif len(usuario) > 0 :
        request.session['usuario'] = usuario[0].id
        return redirect('/livro/home/')    

    return HttpResponse()

def sair(request):
    request.session.flush()
    return redirect('/auth/login')
       
