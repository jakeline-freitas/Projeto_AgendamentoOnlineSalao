from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import AgendamentoForm
from .models import Agendamento
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

####### Create #########


class AgendamentoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamento/FormCreate.html'
    success_url = reverse_lazy('listarSaloes')

####### List #########


class AgendamentoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Agendamento
    template_name = 'agendamento/Lista.html'
