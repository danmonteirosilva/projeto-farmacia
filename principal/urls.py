from django.urls import path
from .views import BalconistaCreateView
from .views import BalconistaListView, FarmaceuticoCreateView, ClienteCreateView, ProdutosCreateView

urlpatterns = [
    path('cadastrar/balconista', BalconistaCreateView.as_view(), name='cadastrar_balconista'),
    path('cadastrar/farmaceutico', FarmaceuticoCreateView.as_view(), name='cadastrar_farmaceutico'),
    path('cadastrar/produtos', ProdutosCreateView.as_view(), name='cadastrar_produtos'),
    path('cadastrar/clientes', ClienteCreateView.as_view(), name='cadastrar_clientes'),
    path('listar/balconista', BalconistaListView.as_view(), name='listar_balconista'),
]
