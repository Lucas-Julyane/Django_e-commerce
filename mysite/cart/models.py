from dataclasses import fields
from django.db import models

from florihell.models import Produto

# Create your models here.

class Cart(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=200)
    observacoes = models.CharField(max_length=300)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
    def __str__(self):
        return "id: {} ___ {}".format(self.id, self.nome)