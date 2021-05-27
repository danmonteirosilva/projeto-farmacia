from .form import ClienteForm
from django.contrib import messages
from .models import Balconista, Farmaceutico, Cliente, Produto
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy


class ClienteCreateView(CreateView):
    form_class = ClienteForm
    template_name = 'cadastrar/cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'cadastrado com suceso!' )
        return reverse_lazy("cadastrar_cliente")


class ClienteListView(ListView):
    model = Cliente
    template_name = 'listar/Cliente.html'
    paginate_by = 3


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


class BalconistaListView(ListView):
    model = Balconista
    template_name = 'listar/balconista.html'
    paginate_by = 3


class FarmaceuticoListView(ListView):
    model = Farmaceutico
    template_name = 'listar/farmaceutico.html'
    paginate_by = 3


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'atualizar/cliente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_Cliente')


class BalconistaUpdateView(UpdateView):
    model = Balconista
    template_name = 'atualizar/balconista.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_balconista')


class FarmaceuticoUpdateView(UpdateView):
    model = Farmaceutico
    template_name = 'atualizar/farmaceutico.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_farmaceutico')

