from django.db import models
from django.forms import CharField, FloatField, IntegerField

# Create your models here.

class Produto(models.Model):
    foto_produto = models.ImageField(null=True, blank=True,upload_to='images/')
    nome_produto = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    valor = models.FloatField()
    qtd = models.IntegerField()

    def __str__(self):
        return "id: {}   nome: {}".format(self.id,self.nome_produto)