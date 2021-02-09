from django.views.generic import ListView
from .models import Agendamento


class AgendamentoListView(ListView):
    paginate_by = 6

    def get_queryset(self):
        queryset = Agendamento.objects.all()

        return queryset
