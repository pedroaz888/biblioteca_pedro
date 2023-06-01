from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home, name='home'),
    path('acessar_livro/<int:id>', views.acessar_livro, name='acessar_livro'),
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('excluir_livro/<int:id>', views.excluir_livro, name='excluir_livro'),
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('cadastro_emprestimo/', views.cadastro_emprestimo, name='cadastro_emprestimo'),
    path('livro_devolvido/', views.livro_devolvido, name='livro_devolvido'),
    path('alterar_livro/', views.alterar_livro, name='alterar_livro'),
    path('seus_emprestimos/', views.seus_emprestimos, name='seus_emprestimos'),
    path('processa_avaliacao/', views.processa_avaliacao, name='processa_avaliacao'),
]