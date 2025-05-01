from django.contrib import admin
from .models import Produto,Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','descricao','disponivel')
    search_fields = ('nome',)
    list_filter = ('disponivel',)
    ordering = ('nome',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome','criado_em')