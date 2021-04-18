from django.urls import path,include
from .views import BalconistaCreateView



urlpatterns = [
    path('principal', BalconistaCreateView.as_view(), name=' balconista'),
 ]