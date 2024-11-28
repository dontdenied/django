from .views import cadastro_produto, contato
from django.urls import path

urlpatterns = [
    path('cadastro/',cadastro_produto, name= 'cadastro'),
    path('contato/', contato, name= 'contato')

]