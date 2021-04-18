from django.db import models


class Balconista(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Balconista')
    rg = models.CharField(max_length=15, blank=False, null=False, verbose_name='RG')
    cpf = models.CharField(max_length=15, blank=False, null=False, verbose_name='CPF')
    data_nascimento = models.DateField(auto_now_add=True, blank=True, null=False, verbose_name='Data da nascimento')
    endereco = models.CharField(max_length=255, null=False, blank=False, verbose_name='Endereço')
    telefone = models.IntegerField(blank=False, null=False, verbose_name='Telefone')
    cep = models.CharField(max_length=15, blank=False, null=False, verbose_name='CEP')
    email = models.CharField(max_length=255, blank=False, null=False, verbose_name='E-mail')


class Farmaceutico(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Balconista')
    rg = models.CharField(max_length=15, blank=False, null=False, verbose_name='RG')
    cpf = models.CharField(max_length=15, blank=False, null=False, verbose_name='CPF')
    data_nascimento = models.DateField(auto_now_add=True, blank=True, null=False, verbose_name='Data da nascimento')
    endereco = models.CharField(max_length=255, null=False, blank=False, verbose_name='Endereço')
    telefone = models.CharField(max_length=12, blank=False, null=False, verbose_name='Telefone')
    cep = models.CharField(max_length=15, blank=False, null=False, verbose_name='CEP')
    crf = models.CharField(max_length=15, blank=False, null=False, verbose_name='CRF')
    email = models.CharField(max_length=255, blank=False, null=False, verbose_name='E-mail')


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Balconista')
    rg = models.CharField(max_length=15, blank=False, null=False, verbose_name='RG')
    cpf = models.CharField(max_length=15, blank=False, null=False, verbose_name='CPF')
    data_nascimento = models.DateField(auto_now_add=True, blank=True, null=False, verbose_name='Data da nascimento')
    endereco = models.CharField(max_length=255, null=False, blank=False, verbose_name='Endereço')
    telefone = models.CharField(max_length=12, blank=False, null=False, verbose_name='Telefone')
    cep = models.CharField(max_length=15, blank=False, null=False, verbose_name='CEP')
    email = models.CharField(max_length=255, blank=False, null=False, verbose_name='E-mail')
    foto = models.FileField(upload_to='foto de cadastro', verbose_name='Foto de cadastro do cliente')

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Produto')
    foto = models.ImageField(null=True, blank=True)
