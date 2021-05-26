from django.urls import path
from .views import BalconistaCreateView, FarmaceuticoCreateView, \
    ClienteCreateView, BalconistaListView, \
    FarmaceuticoListView, BalconistaUpdateView, \
    ClienteListView, ClienteUpdateView, FarmaceuticoUpdateView

urlpatterns = [
    path('cadastrar/balconista', BalconistaCreateView.as_view(), name='cadastrar_balconista'),
    path('cadastrar/farmaceutico', FarmaceuticoCreateView.as_view(), name='cadastrar_farmaceutico'),
    path('cadastrar/cliente', ClienteCreateView.as_view(), name='cadastrar_cliente'),
    path('listar/balconista', BalconistaListView.as_view(), name='listar_balconista'),
    path('listar/farmaceutico', FarmaceuticoListView.as_view(), name='listar_farmaceutico'),
    path('listar/cliente', ClienteListView.as_view(), name='listar_cliente'),
    path('atualizar/balconista/<int:pk>', BalconistaUpdateView.as_view(), name='atualizar_balconista'),
    path('atualizar/cliente/<int:pk>', ClienteUpdateView.as_view(), name='atualizar_cliente'),
    path('atualizar/farmaceutico/<int:pk>', FarmaceuticoUpdateView.as_view(), name='atualizar_farmaceutico'),

]
