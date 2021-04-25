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
    foto = models.FileField(upload_to='foto de cadastro', verbose_name='Foto do produto')
    estoque = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade no Estoque')
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    generico = models.CharField(max_length=3, blank=False, null=False, verbose_name='O medicamento é genérico?')


class Venda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Venda')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False, verbose_name='Valor')
    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False, verbose_name='Número da Venda')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observações")
    venda_concluida = models.BooleanField(blank=False, null=False)
    qtd_itens = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade de Itens Vendidos')
    produtos = models.ManyToManyField('Produto')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1, verbose_name='Cliente')

class Receita(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False, verbose_name='Descrição')
    foto = models.FileField(upload_to='foto da receita', verbose_name='Fazer upload da receita')
    venda = models.ForeignKey('Venda', on_delete=models.DO_NOTHING, default=1, verbose_name='Venda')


class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=14, blank=False, null=False, verbose_name='CNPJ')
    nome_fantasia = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome Fantasia')
    razao_social = models.CharField(max_length=255, blank=False, null=False, verbose_name='Razão Social')
    endereco = models.CharField(max_length=255, null=False, blank=False, verbose_name='Endereço')
    telefone = models.CharField(max_length=12, blank=False, null=False, verbose_name='Telefone')
    cep = models.CharField(max_length=15, blank=False, null=False, verbose_name='CEP')
    email = models.CharField(max_length=255, blank=False, null=False, verbose_name='E-mail')
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")


class Compra(models.Model):
    produtos = models.ManyToManyField('Produto')
    quantidade = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade de Itens Comprados')
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.DO_NOTHING, default=1, verbose_name='Fornecedor')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False, verbose_name='Valor')
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    data_compra = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_compra = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_hora_compra = models.DateTimeField(auto_now_add=True, blank=True, null=False)


class Pagamento(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False, verbose_name='Descrição do Pagamento')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False, verbose_name='Valor')
    comprovante = models.FileField(upload_to='foto da receita', verbose_name='Fazer upload do comprovante')
    data_pagamento = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_pagamento = models.TimeField(auto_now_add=True, blank=True, null=False)


class Contas_a_pagar(models.Model):
    titulo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Título')
    data_venc = models.DateField(auto_now_add=False, blank=True, null=False, verbose_name='Data de vencimento')
    valor_pagar = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False, verbose_name='Valor a pagar')

    class Meta:
        verbose_name = 'Contas a pagar'
        verbose_name_plural = 'Contas a Pagar'

