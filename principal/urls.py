from django.urls import path
from .views import BalconistaCreateView,FarmaceuticoCreateView
from .views import BalconistaListView,FarmaceuticoListView

urlpatterns = [
    path('cadastrar/balconista', BalconistaCreateView.as_view(), name ='cadastrar_balconista'),
    path('cadastrar/farmaceutico', FarmaceuticoCreateView.as_view(), name ='cadastrar_farmaceutico'),
    path('listar/balconista', BalconistaListView.as_view(), name ='listar_balconista'),
    path('listar/farmaceutico', FarmaceuticoListView.as_view(), name ='listar_farmaceutico'),


]
