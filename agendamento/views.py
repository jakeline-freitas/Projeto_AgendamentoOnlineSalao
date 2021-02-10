from django.views.generic import CreateView, ListView
from .models import Agendamento
from django.urls import reverse_lazy


class AgendamentoCreate(CreateView):
    model = Agendamento
    fields = '__all__'
    template_name = 'agendamento/FormCreate.html'
    success_url = reverse_lazy('index')

