from braces.views import GroupRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic.list import ListView

from servicos.models import Servico, Salao
from accounts.models import User
from .forms import AgendamentoForm
from .models import Agendamento, AgendamentoServico
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.mail import send_mail


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

        self.object = form.save(commit=False)
        self.object.cliente = self.request.user

        servicos = list(form.cleaned_data["servico"])
        valor = 0
        for ser in servicos:
            valor += ser.preco

        self.object.totalAPagar.add(valor)

        self.object.save()
        registro = form.save()

        for serv in servicos:
            agendamentoServico = AgendamentoServico(servico=serv, agendamento=registro)
            agendamentoServico.save()

        return HttpResponseRedirect(self.get_success_url())


####### List #########


class AgendamentoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Clientes"
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


class TodosAgendamentosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Proprietários"
    login_url = reverse_lazy('login')
    model = AgendamentoServico
    template_name = 'agendamento/ListaTodos.html'

    def get_queryset(self):
        saloes = [salao.id for salao in Salao.objects.filter(responsavel=self.request.user)]

        servicos = [servico.id for servico in Servico.Servicos.filter(estabelecimento__in=saloes)]

        queryset = AgendamentoServico.objects.filter(servico__in=servicos)
        return queryset

#-------------Update --------------------


class AgendamentoServicoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Proprietários"
    model = Agendamento
    fields = ['estado']
    template_name = 'agendamento/Update.html'
    success_url = reverse_lazy('listarTodosAgendamentos')

    def form_valid(self, form):
        #id_agendamento = self.kwargs.get("pk")
        usuario = self.request.user
        emailU = usuario.email
        #emailCliente = [age.cliente for age in Agendamento.objects.filter(id=id_agendamento)]


        send_mail(
            'Agendamento',
            'teste msg 2.',
             emailU,
            ['to@example.com'],
            fail_silently=False,
        )

        return super().form_valid(form)

class AgendamentoDetail(LoginRequiredMixin, DetailView):
    template_name = "products/detail.html"

    # def get_context_data(self, *args, **kwargs):
    # context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    # print(context)
    # return context
