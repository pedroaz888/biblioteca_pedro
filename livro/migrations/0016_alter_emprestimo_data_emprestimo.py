# Generated by Django 4.2.1 on 2023-05-30 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_alter_emprestimo_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 11, 33, 23, 657896)),
        ),
    ]