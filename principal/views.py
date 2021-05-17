from .models import Balconista, Farmaceutico, Cliente, Produto
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy


class BalconistaCreateView(CreateView):
    model = Balconista
    template_name = 'cadastrar/balconista.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cadastrar_balconista')

class FarmaceuticoCreateView(CreateView):
    model =  Farmaceutico
    template_name ='cadastrar/farmaceutico.html'
    
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



