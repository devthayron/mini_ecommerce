from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Produto
from django.urls import reverse_lazy
from .forms import ProdutoForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexListView(LoginRequiredMixin,ListView):
    template_name = 'produtos/index.html'
    model = Produto
    context_object_name = 'produtos'
    paginate_by = 3

    def get_queryset(self):
        return Produto.objects.filter(disponivel=True).order_by('-preco')  # Mostra apenas os Produtos disponiveis.


class CriarProdutoView(LoginRequiredMixin,CreateView):
    template_name = 'produtos/produto_form.html'
    model = Produto         
    success_url = reverse_lazy('index') # após a criação, direciona para url 'index'
    form_class = ProdutoForm 
    
    def form_valid(self, form):
        response = super().form_valid(form)
        produto = self.object
        messages.success(self.request, f'Produto "{produto.nome}" criado com sucesso!')
        return response
    

class EditarProdutoView(LoginRequiredMixin,UpdateView):
    template_name = 'produtos/produto_form.html'
    model = Produto
    success_url = reverse_lazy('index')
    form_class = ProdutoForm

    def form_valid(self, form):
        response = super().form_valid(form)
        produto = self.object
        messages.warning(self.request,f'Produto "{produto.nome}" editado com sucesso!')
        return response
    

class DeleteProdutoView(LoginRequiredMixin,DeleteView):
    template_name = 'produtos/produto_confirm_delete.html'
    model = Produto
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        produto = self.get_object()
        response = super().post(request, *args, **kwargs)
        messages.error(self.request,f'Produto "{produto.nome}" deletado com sucesso!')
        return response