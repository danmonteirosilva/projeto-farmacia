from django.shortcuts import render
from .models import Balconista, Farmaceutico
from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy


class BalconistaCreateView(CreateView):
    model = Balconista
    template_name = 'cadastra_balconista.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Balconista')


class FarmaceuticoCreateView(CreateView):
    model = Farmaceutico
    template_name = 'farmaceutico.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Farmaceutico')


class BalconistaListView(ListView):
    model = Balconista
    template_name = 'listar_balconista'

