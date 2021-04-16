from django.db import models

class Balconista(models.Model):
    codigo = models.CharField(max_length=100),
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    dt_nascimento = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)


class Caixa(models.Model):
    codigo_caixa: models.DecimalField(max_digits=10)
    qtd: models.DecimalField(max_digits=10)
    valor_unit: models.DecimalField(max_digits=7, decimal_places=2)
    valot_total: models.DecimalField(max_digits=7, decimal_places=2)
    taxa_entrega: models.DecimalField(max_digits=7, decimal_places=2)
    forma_pagamento: models.CharField(max_length=100)
    convenio: models.BooleanField(default=False)
    dinheiro: models.DecimalField(max_digits=7, decimal_places=3)
    troco: models.DecimalField(max_digits=7, decimal_places=3)
    vendedor: models.ForeignKey(Balconista, on_delete=models.CASCADE)
    observacoes: models.TextField()



# Create your models here.
