# Generated by Django 4.2.1 on 2023-05-29 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0011_emprestimo_avaliacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo',
            old_name='nome_emprestado_com_cadastro',
            new_name='nome_cadastrado',
        ),
        migrations.RenameField(
            model_name='emprestimo',
            old_name='nome_emprestado_sem_cadastro',
            new_name='nome_sem_cadastro',
        ),
    ]