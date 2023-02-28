from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=150)
    abreviacao = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
