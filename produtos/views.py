from django.shortcuts import render
from .forms import ContatoForm, ProdutoForm, Formulario
from django.core.mail import send_mail

def cadastro_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
    else:
        form = ProdutoForm()

    return render(request, 'formulario2.html', {'form': form})

# def tarefa(request):
#     if request.method == 'POST':
#         form = Formulario(request.POST)
#         if form.is_valid():
#             forma = form.cleaned_data['formulario']
#         form = Formulario
#     else:
#         form = Formulario()
#     return (request,'formulario2.html', {'form': form} )

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            
        
    else:
        form = ContatoForm()
    return render(request, 'formulario.html', {'form': form})

# Create your views here.
