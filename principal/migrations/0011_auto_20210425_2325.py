# Generated by Django 3.2 on 2021-04-26 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_parceiro_repositorio_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
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
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.fornecedor', verbose_name='Fornecedor'),
        ),
        migrations.AddField(
            model_name='produto',
            name='fabricante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.fabricante', verbose_name='Fabricante'),
        ),
    ]
