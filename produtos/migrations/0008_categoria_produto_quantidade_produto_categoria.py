# Generated by Django 5.2 on 2025-05-01 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_alter_produto_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado_em')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=1, verbose_name='Quantidade'),
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produtos.categoria'),
        ),
    ]
