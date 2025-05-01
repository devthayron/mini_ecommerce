from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['categoria', 'nome', 'imagem', 'preco', 'quantidade', 'disponivel']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do produto', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'placeholder': 'Categoria', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva o produto...', 'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'placeholder': 'Preço do produto', 'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'disponivel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'quantidade': forms.NumberInput(attrs={'placeholder': 'Quantidade', 'class': 'form-control'})
        }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = 'Selecione uma categoria'