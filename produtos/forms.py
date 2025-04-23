# produtos/forms.py
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'imagem','preco', 'descricao', 'disponivel']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva o produto...'}),
            'preco': forms.NumberInput(attrs={'placeholder': 'Preço do produto'}),
        }
