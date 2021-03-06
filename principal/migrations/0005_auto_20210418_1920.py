# Generated by Django 3.2 on 2021-04-18 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_merge_0002_caixa_0003_auto_20210417_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Balconista')),
                ('rg', models.CharField(max_length=15, verbose_name='RG')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('data_nascimento', models.DateField(auto_now_add=True, verbose_name='Data da nascimento')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('cep', models.CharField(max_length=15, verbose_name='CEP')),
                ('email', models.CharField(max_length=255, verbose_name='E-mail')),
                ('foto', models.FileField(upload_to='foto de cadastro', verbose_name='Foto de cadastro do cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=255, verbose_name='Nome do Produto')),
                ('foto', models.FileField(upload_to='foto de cadastro', verbose_name='Foto do produto')),
                ('estoque', models.IntegerField(blank=True, default=0, verbose_name='Quantidade no Estoque')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('generico', models.CharField(max_length=3, verbose_name='O medicamento é genérico?')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Venda')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor')),
                ('data_venda', models.DateField(auto_now_add=True)),
                ('hora_venda', models.TimeField(auto_now_add=True)),
                ('data_hora_venda', models.DateTimeField(auto_now_add=True)),
                ('numero_venda', models.IntegerField(verbose_name='Número da Venda')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('venda_concluida', models.BooleanField()),
                ('qtd_itens', models.IntegerField(blank=True, default=0, verbose_name='Quantidade de Itens Vendidos')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.cliente', verbose_name='Cliente')),
                ('produtos', models.ManyToManyField(to='principal.Produto')),
            ],
        ),
        migrations.DeleteModel(
            name='Caixa',
        ),
        migrations.AlterField(
            model_name='balconista',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='farmaceutico',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
