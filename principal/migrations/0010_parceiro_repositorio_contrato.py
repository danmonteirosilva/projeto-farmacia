# Generated by Django 3.2 on 2021-04-25 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_entregador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('nome_fantasia', models.CharField(max_length=255, verbose_name='Nome Fantasia')),
                ('razao_social', models.CharField(max_length=255, verbose_name='Razão Social')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('cep', models.CharField(max_length=15, verbose_name='CEP')),
                ('email', models.CharField(max_length=255, verbose_name='E-mail')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Repositorio_contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Contrato')),
                ('contrato', models.FileField(upload_to='arquivo de contrato', verbose_name='Selecionar o contrato')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Repositório de Contratos',
            },
        ),
    ]
