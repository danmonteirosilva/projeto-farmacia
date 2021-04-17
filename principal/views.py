from django.shortcuts import render
from .models import Balconista
from django.views.generic import CreateView
from django.urls import reverse_lazy

class BalconistaCreateView(CreateView):
    model = Balconista
    template_name = 'balconista.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('Balconista')