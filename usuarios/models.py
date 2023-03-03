from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(AbstractUser):
    id = models.AutoField(primary_key=True, null=False)
    cpf_cnpj = models.CharField(max_length=14, default='00000000000000')
