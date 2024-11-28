from django import forms
from .models import Produto, Formulario


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label="nome")
    email = forms.EmailField(label='email')
    mensagem = forms.CharField(max_length=100, label='mensagem', widget=forms.Textarea)



class ProdutoForm(forms.ModelForm):
    class meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque']
        labels = {'nome': 'Nome do produto', 
                  'preco': 'Preço do produto',
                  'estoque': 'Estoque',
                  }
        


class FormularioForm(forms.Form):
    forma = forms.CharField(max_length=100)
        

        
