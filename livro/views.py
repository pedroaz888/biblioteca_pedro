from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivro, CategoriaLivro
from django import forms
from datetime import datetime
from django.db.models import Q

def home(request):
   if request.session.get('usuario'):
       usuario = Usuario.objects.get(id = request.session['usuario'])
       status_categoria = request.GET.get('cadastro_categoria')
       status_livro = request.GET.get('cadastro_livro')
       # o filter traz uma lista de livros filtrando pelo usuario
       livros = Livros.objects.filter(usuario=usuario)
       total_livros = livros.count()
       form = CadastroLivro()
       form.fields['usuario'].initial = request.session['usuario'] 
       form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)

       form_categoria = CategoriaLivro()
       usuarios = Usuario.objects.all()
       livros_emprestar = Livros.objects.filter(usuario=usuario).filter(emprestado = False)
       livros_emprestados = Livros.objects.filter(usuario=usuario).filter(emprestado = True)

       

       return render(request, 'home.html', {'livros': livros, 
                                            'usuario_logado': request.session.get('usuario'),
                                            'form': form,
                                            'form_categoria': form_categoria,
                                            'status_categoria': status_categoria,
                                            'status_livro': status_livro,
                                            'usuarios': usuarios,
                                            'livros_emprestar': livros_emprestar,
                                             'total_livros': total_livros,
                                             'livros_emprestados': livros_emprestados})
   else:
        return redirect('/aut/login/?status=2')
   
def acessar_livro(request, id):
    if request.session.get('usuario'):
        status_categoria = request.GET.get('cadastro_categoria')
        status_livro = request.GET.get('cadastro_livro')
        #o get não traz uma lista de livros e sim o livro especifico com id
        livro = Livros.objects.get(id=id)
        if request.session.get('usuario') == livro.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario_id=request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro = livro)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            usuario = Usuario.objects.get(id = request.session['usuario'])
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
         
            form_categoria = CategoriaLivro()
            usuarios = Usuario.objects.all()
            livros_emprestar = Livros.objects.filter(usuario=usuario).filter(emprestado = False)
            livros_emprestados = Livros.objects.filter(usuario=usuario).filter(emprestado = True)

            return render(request, 'acessar_livro.html', {'livro':livro, 
                                                          'categoria_livro': categoria_livro, 
                                                          'emprestimos': emprestimos,
                                                          'usuario_logado': request.session.get('usuario'),
                                                          'form': form,
                                                          'id_livro': id,
                                                          'form_categoria': form_categoria,
                                                          'cadastro_categoria': cadastrar_categoria,
                                                          'status_livro': status_livro,
                                                          'usuarios': usuarios,
                                                          'livros_emprestar': livros_emprestar,
                                                          'livros_emprestados': livros_emprestados})
        else:
            return HttpResponse('Esse livro não é seu')
           
    return redirect('/auth/login/?status=2') 

#para cadastrar img precisa ser request.FILES------------------------------------------
def cadastrar_livro(request):
    if request.method == "POST":
        form = CadastroLivro(request.POST, request.FILES)
        
        
        if form.is_valid():
            form.save()
            return redirect('/livro/home?cadastro_livro=1')
        else:
            return HttpResponse('Dados Inválidos')

def cadastrar_categoria(request):
    if request.method == "POST":
        form_categoria = CategoriaLivro(request.POST)
        
        if form_categoria.is_valid():
            form_categoria.save()
            return redirect('/livro/home?cadastro_categoria=1')
        else:
            return HttpResponse('Dados Inválidos')
        
def cadastro_emprestimo(request):
        if request.method == "POST":
            nome_cadastrado = request.POST.get('nome_cadastrado')
            nome_sem_cadastro = request.POST.get('nome_sem_cadastro')
            livro_emprestado = request.POST.get('livro_emprestado')

            if nome_sem_cadastro:

                emprestimo = Emprestimo(nome_sem_cadastro = nome_sem_cadastro,
                                        livro_id = livro_emprestado)

            else:
                emprestimo = Emprestimo(nome_cadastrado_id = nome_cadastrado,
                                        livro_id = livro_emprestado)

            
            emprestimo.save()

            livro = Livros.objects.get(id = livro_emprestado)
            livro.emprestado = True
            livro.save()

            return redirect('/livro/home')
            
        
def excluir_livro(request, id):
    livro = Livros.objects.get(id=id).delete()
    return redirect ('/livro/home')  

def livro_devolvido(request):
    id = request.POST.get('id_livro_devolvido')
    livro_devolvido = Livros.objects.get(id=id)
    livro_devolvido.emprestado = False
    livro_devolvido.save()

    data_devolvido = Emprestimo.objects.get(Q(livro = livro_devolvido) & Q(data_devolucao = None) )
    data_devolvido.data_devolucao = datetime.now()
    data_devolvido.save()

    return redirect ('/livro/home') 

def alterar_livro(request):
    livro_id = request.POST.get('livro_id')
    nome_livro = request.POST.get('nome_livro')
    autor =request.POST.get('autor')
    categoria_id = request.POST.get('categoria_id')
    categoria = Categoria.objects.get(id = categoria_id)

    livro = Livros.objects.get(id = livro_id)
    #sistema de segurança para não alterar no inspecionar
    if livro.usuario.id == request.session['usuario']:
        livro.nome = nome_livro
        livro.autor = autor
        livro.categoria = categoria
        livro.save()   
        return redirect('/livro/home')
    else:
        return redirect('/auth/sair')

def seus_emprestimos(request):
    usuario = Usuario.objects.get(id = request.session['usuario'])
    emprestimos = Emprestimo.objects.filter(nome_cadastrado = usuario)


    return render(request, 'seus_emprestimos.html', {'usuario_logado': request.session['usuario'],
                                                     'emprestimos': emprestimos})

def processa_avaliacao(request):
    id_emprestimo = request.POST.get('id_emprestimo')
    opcoes = request.POST.get('opcoes')
    id_livro = request.POST.get('id_livro')

    
    emprestimo = Emprestimo.objects.get(id = id_emprestimo)
    emprestimo.avaliacao = opcoes
    emprestimo.save()

    return redirect(f'/livro/acessar_livro/{id_livro}')


