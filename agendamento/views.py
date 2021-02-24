from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView

from servicos.models import Servico, Salao
from .forms import AgendamentoForm
from .models import Agendamento, AgendamentoServico
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


####### Create #########


class AgendamentoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamento/FormCreate.html'
    success_url = reverse_lazy('listarSaloes')

    def get_context_data(self, **kwargs):
        id_estabelecimento = self.kwargs.get("pk")
        context = super(AgendamentoCreate, self).get_context_data(**kwargs)
        context['form'].fields['servico'].queryset = Servico.Servicos.filter(estabelecimento=id_estabelecimento).order_by("nome")
        return context

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.cliente = self.request.user

        servicos = list(form.cleaned_data["servico"])
        valor = 0
        for ser in servicos:
            valor += ser.preco

        self.object.totalAPagar = valor

        self.object.save()
        registro = form.save()

        for serv in servicos:
            agendamentoServico = AgendamentoServico(servico=serv, agendamento=registro)

        return HttpResponseRedirect(self.get_success_url())


####### List #########


class AgendamentoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Agendamento
    template_name = 'agendamento/Lista.html'

    def get_queryset(self):
        usuario = self.request.user
        queryset = Agendamento.objects.filter(cliente=usuario)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(AgendamentoList, self).get_context_data(*args, **kwargs)
        return context


class AgendamentoDetail(LoginRequiredMixin, DetailView):
    template_name = "products/detail.html"

    # def get_context_data(self, *args, **kwargs):
    # context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    # print(context)
    # return context
