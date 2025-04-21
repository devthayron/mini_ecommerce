from django.shortcuts import render
from django.views.generic import ListView
from .models import Produto

class IndexListView(ListView):
    template_name = 'index.html'
    model = Produto
    context_object_name = 'produtos'

    def get_queryset(self):
        return Produto.objects.filter(disponivel=True)  # Mostra apenas os Produtos disponiveis.