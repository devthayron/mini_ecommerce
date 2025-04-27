from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'imagem', 'preco', 'descricao', 'disponivel']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do produto', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva o produto...', 'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'placeholder': 'Preço do produto', 'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'disponivel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
