from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=50)
    preco = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    descricao = models.TextField("Descrição", help_text='Limite de 50 caracteres',blank=True)
    disponivel = models.BooleanField("Disponível",default=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'