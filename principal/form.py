from django import forms
from .models import *


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'rg', 'cpf', 'endereco', 'telefone', 'cep', 'email', 'foto']