from django.contrib import admin
from .models import Balconista,Farmaceutico, Cliente, Produto, Venda


admin.site.register(Balconista)
admin.site.register(Farmaceutico)
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Venda)