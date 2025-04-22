from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Produto
from django.urls import reverse_lazy

class IndexListView(ListView):
    template_name = 'index.html'
    model = Produto
    context_object_name = 'produtos'

    def get_queryset(self):
        return Produto.objects.filter(disponivel=True)  # Mostra apenas os Produtos disponiveis.

class CriarProdutoView(CreateView):
    template_name = 'produto_form.html'
    model = Produto
    fields = '__all__'          # mostra todos os campos do model 'Produto'
    success_url = reverse_lazy('index') # após a criação, direciona para url 'index'

class EditarProdutoView(UpdateView):
    template_name = 'produto_form.html'
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('index')

class DeleteProdutoView(DeleteView):
    template_name = 'produto_confirm_delete.html'
    model = Produto
    success_url = reverse_lazy('index')