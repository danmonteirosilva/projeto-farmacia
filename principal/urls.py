from django.urls import path
from .views import BalconistaCreateView
from .views import BalconistaListView

urlpatterns = [
    path('cadastrar_balconista', BalconistaCreateView.as_view(), name='balconista'),
    path('listar/balconista', BalconistaListView.as_view(), name='listar_balconista'),
]
