from .models import Balconista, Farmaceutico, Cliente, Produto
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.urls import reverse_lazy


class BalconistaCreateView(CreateView):
    model = Balconista
    template_name = 'cadastrar/balconista.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cadastrar_balconista')


class BalconistaListView(ListView):
    model = Balconista
    template_name = 'listar/balconista.html'
    paginate_by = 3



