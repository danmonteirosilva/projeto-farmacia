from django.urls import path
from .views import BalconistaCreateView
from .views import BalconistaListView

urlpatterns = [
    path('cadastrar/balconista', BalconistaCreateView.as_view(), name='cadastrar_balconista'),
    path('listar/balconista', BalconistaListView.as_view(), name='listar_balconista'),


]
