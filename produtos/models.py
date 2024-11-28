from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    estoque = models.PositiveIntegerField()
    data_ciacao = models.DateTimeField(auto_now_add=True)


class Formulario(models.Model):
    forma = models.CharField(max_length=100)




# Create your models here.
