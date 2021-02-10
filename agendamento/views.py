from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Agendamento
from django.urls import reverse_lazy

####### Create #########


class AgendamentoCreate(CreateView):
    model = Agendamento
    fields = '__all__'
    template_name = 'agendamento/FormCreate.html'
    success_url = reverse_lazy('index')


####### List #########


class AgendamentoList(ListView):
    model = Agendamento
    template_name = 'agendamento/Lista.html'
