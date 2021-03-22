from braces.views import GroupRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic.list import ListView

from servicos.models import Servico, Salao
from .enviarEmail import EnviarEmail
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
        context['form'].fields['servico'].queryset = Servico.Servicos.filter(
            estabelecimento=id_estabelecimento).order_by("nome")
        return context

    def form_valid(self, form):

        agendamento = form.save(commit=False)
        agendamento.cliente = self.request.user
        agendamento.totalAPagar = 0
        agendamento.save()

        servicos = list(form.cleaned_data["servico"])
        valor = 0
        for ser in servicos:
            valor += ser.preco
            agendamento.servico.add(ser)

        agendamento.totalAPagar=valor

        agendamento= form.save()


        # for serv in servicos:
        #     agendamentoServico = AgendamentoServico(servico=serv, agendamento=agendamento)
        #     # agendamentoServico.save()

        return HttpResponseRedirect("/agendamento/listarAgendamentos/")


####### List #########


class AgendamentoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Clientes"
    login_url = reverse_lazy('login')
    model = AgendamentoServico
    template_name = 'agendamento/Lista.html'

    def get_queryset(self):
        usuario = self.request.user
        queryset = AgendamentoServico.objects.filter(agendamento__cliente=usuario)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(AgendamentoList, self).get_context_data(*args, **kwargs)
        return context


class TodosAgendamentosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Proprietários"
    login_url = reverse_lazy('login')
    model = AgendamentoServico
    template_name = 'agendamento/ListaTodos.html'

    def get_queryset(self):
        saloes = [salao.id for salao in Salao.objects.filter(responsavel=self.request.user)]

        servicos = [servico.id for servico in Servico.Servicos.filter(estabelecimento__in=saloes)]

        queryset = AgendamentoServico.scheduledServiceManager.filter(servico__in=servicos)
        return queryset

#-------------Update --------------------


class AgendamentoServicoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Proprietários"
    model = Agendamento
    fields = ['estado']
    template_name = 'agendamento/Update.html'
    success_url = reverse_lazy('listarTodosAgendamentos')


class AgendamentoDetail(LoginRequiredMixin, DetailView):
    template_name = "products/detail.html"

    # def get_context_data(self, *args, **kwargs):
    # context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    # print(context)
    # return context