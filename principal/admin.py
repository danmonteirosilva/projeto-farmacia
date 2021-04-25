from django.contrib import admin
from .models import Balconista,Farmaceutico, Cliente, Produto, Venda, Receita, Fornecedor, Compra, Pagamento, Contas_a_pagar


admin.site.register(Balconista)
admin.site.register(Farmaceutico)
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Receita)
admin.site.register(Fornecedor)
admin.site.register(Compra)
admin.site.register(Pagamento)
admin.site.register(Contas_a_pagar)
