from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Servico, Salao
from django.urls import reverse_lazy

####### Create #########


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


###### Update ######


class ServicosUpdate(UpdateView):
    model = Servico
    fields = ['preco', 'descricao', 'is_available']
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')


class SalaoUpdate(UpdateView):
    model = Salao
    fields = '__all__'
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')


####### Delete #########


class ServicosDelete(DeleteView):
    model = Servico
    template_name = 'servicos/formularioDelete.html'
    success_url = reverse_lazy('index')


class SalaoDelete(DeleteView):
    model = Salao
    template_name = 'servicos/formularioDelete.html'
    success_url = reverse_lazy('index')
