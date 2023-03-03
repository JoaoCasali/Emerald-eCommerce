from django.db import models
from uuid import uuid4

def upload_imagem_produto(produto, nomeArquivo):
    return f"produto/{uuid4()}_produto"

class Produto(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descricao = models.TextField(null=True)
    abreviacao = models.CharField(max_length=50, null=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    imagem = models.ImageField(upload_to=upload_imagem_produto, blank=True, null=True)