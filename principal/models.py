from django.db import models

<<<<<<< HEAD

class Balconista(models.Model):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do Balconista')
=======
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Balconista')
>>>>>>> efae385e7f2c20931325f446663af7ba0ddb6162
    rg = models.CharField(max_length=15, blank=False, null=False, verbose_name='RG')
    cpf = models.CharField(max_length=15, blank=False, null=False, verbose_name='CPF')
    data_nascimento = models.DateField(auto_now_add=True, blank=True, null=False, verbose_name='Data da nascimento')
    endereco = models.CharField(max_length=255, null=False, blank=False, verbose_name='Endereço')
    telefone = models.IntegerField(blank=False, null=False, verbose_name='Telefone')
<<<<<<< HEAD
=======
=======
>>>>>>> b3190ebba2ee8755b88a22fed1b070fded83a89d
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
=======
>>>>>>> danillo

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


<<<<<<< HEAD
# Create your models here.
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/master
=======
    cep = models.CharField(max_length=15, blank=False, null=False, verbose_name='CEP')
    email = models.CharField(max_length=255, blank=False, null=False, verbose_name='E-mail')


class Farmaceutico(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Balconista')
=======
=======
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do Balconista')
>>>>>>> b3190ebba2ee8755b88a22fed1b070fded83a89d
=======
class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Balconista')
>>>>>>> danillo
    rg = models.CharField(max_length=15, blank=False, null=False, verbose_name='RG')
    cpf = models.CharField(max_length=15, blank=False, null=False, verbose_name='CPF')
    data_nascimento = models.DateField(auto_now_add=True, blank=True, null=False, verbose_name='Data da nascimento')
    endereco = models.CharField(max_length=255, null=False, blank=False, verbose_name='Endereço')
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> danillo
    telefone = models.CharField(max_length=12, blank=False, null=False, verbose_name='Telefone')
    cep = models.CharField(max_length=15, blank=False, null=False, verbose_name='CEP')
    email = models.CharField(max_length=255, blank=False, null=False, verbose_name='E-mail')
    foto = models.FileField(upload_to='foto de cadastro', verbose_name='Foto de cadastro do cliente')
<<<<<<< HEAD
>>>>>>> efae385e7f2c20931325f446663af7ba0ddb6162
=======
    telefone = models.IntegerField(blank=False, null=False, verbose_name='Telefone')
>>>>>>> Robertokalleb-master
>>>>>>> b3190ebba2ee8755b88a22fed1b070fded83a89d
=======
>>>>>>> danillo
