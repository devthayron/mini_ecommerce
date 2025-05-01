from django.db import models

class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=50)
    criado_em = models.DateTimeField("Criado_em", auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField("Nome", max_length=50)
    preco = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    descricao = models.TextField("Descrição",blank=True)
    disponivel = models.BooleanField("Disponível",default=True)
    imagem = models.ImageField('imagem', upload_to='produtos', blank=True,null=True)
    quantidade = models.IntegerField("Quantidade")


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'