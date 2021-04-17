from django.db import models

class Balconista(models.Model):
<<<<<<< HEAD
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
=======
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do Balconista')
    rg = models.CharField(max_length=15, blank=False, null=False, verbose_name='RG')
    cpf = models.CharField(max_length=15, blank=False, null=False, verbose_name='CPF')
    data_nascimento = models.DateField(auto_now_add=True, blank=True, null=False, verbose_name='Data da nascimento')
    endereco = models.CharField(max_length=255, null=False, blank=False, verbose_name='Endereço')
    telefone = models.IntegerField(blank=False, null=False, verbose_name='Telefone')
>>>>>>> Robertokalleb-master
