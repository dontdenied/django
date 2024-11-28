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
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError('o nome deve ter no mínimo 3 caracteres')
        return nome
    
    def clean_estoque(self):
        estoque = self.cleaned_data.get('estoque')
        if estoque == 0:
            raise forms.ValidationError('estoque vazio')
        return estoque
        


class FormularioForm(forms.Form):
    forma = forms.CharField(max_length=100)


        

        
