from typing import Any
from django.db import models
from datetime import date
import datetime
from usuarios.models import Usuario


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome 

class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    nome = models.CharField(max_length=45)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank =True)
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default=False)
   
    #liga com a classe acima de Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    #liga com a classe Usuario
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self) :
        return self.nome
    
    
class Emprestimo(models.Model):
    choices = [
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo'),

    ]
    nome_cadastrado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank = True, null = True)
    nome_sem_cadastro = models.CharField(max_length=30, blank = True, null = True)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now())
    data_devolucao = models.DateTimeField(blank = True, null = True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)

    def __str__(self) -> str:
            return f"{self.nome_cadastrado} |  {self.livro}"
    

  