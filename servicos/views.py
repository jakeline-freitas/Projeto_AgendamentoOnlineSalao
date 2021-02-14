from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Servico, Salao
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

####### Create #########


class ServicosCreate(LoginRequiredMixin, CreateView):
    model = Servico
    fields = '__all__'
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')


class SalaoCreate(LoginRequiredMixin, CreateView):
    model = Salao
    fields = '__all__'
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')


###### Update ######


class ServicosUpdate(LoginRequiredMixin, UpdateView):
    model = Servico
    fields = ['preco', 'descricao', 'is_available']
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')


class SalaoUpdate(LoginRequiredMixin, UpdateView):
    model = Salao
    fields = '__all__'
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')


####### Delete #########


class ServicosDelete(LoginRequiredMixin, DeleteView):
    model = Servico
    template_name = 'servicos/formularioDelete.html'
    success_url = reverse_lazy('index')


class SalaoDelete(LoginRequiredMixin, DeleteView):
    model = Salao
    template_name = 'servicos/formularioDelete.html'
    success_url = reverse_lazy('listarSaloes')


####### List #########


class SalaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    paginate_by = 6
    model = Salao
    template_name = 'servicos/listarSaloes.html'


class ServicoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    paginate_by = 6
    model = Servico
    template_name = 'servicos/listarServicos.html'
