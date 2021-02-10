from django.views.generic import CreateView, UpdateView
from .models import Servico, Salao
from django.urls import reverse_lazy


class ServicosCreate(CreateView):
    model = Servico
    fields = '__all__'
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')


class SalaoCreate(CreateView):
    model = Salao
    fields = '__all__'
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')



