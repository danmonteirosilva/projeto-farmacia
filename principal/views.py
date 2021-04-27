from .models import Balconista, Farmaceutico
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class BalconistaCreateView(CreateView):
    model = Balconista
    template_name = 'cadastrar/balconista.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cadastrar_balconista')


class FarmaceuticoCreateView(CreateView):
    model = Farmaceutico
    template_name = 'cadastrar/farmaceutico.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cadastrar_farmaceutico')


class ClienteCreateView(CreateView):
    model = Farmaceutico
    template_name = 'cadastrar/clientes.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cadastrar_cliente')


class ProdutosCreateView(CreateView):
    model = Farmaceutico
    template_name = 'cadastrar/produtos.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cadastrar_produtos')


class BalconistaListView(ListView):
    model = Balconista
    template_name = 'listar_balconista'
