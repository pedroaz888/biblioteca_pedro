# Generated by Django 4.2.1 on 2023-05-25 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0007_alter_emprestimo_nome_emprestado_com_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]