# Generated by Django 4.2.1 on 2023-05-25 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0008_alter_emprestimo_data_devolucao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='tempo_duracao',
        ),
    ]
