from django.views.generic import ListView
from .models import Servico


class ServicosListView(ListView):
    paginate_by = 6

    def get_queryset(self):
        queryset = Servico.available.all()

        return queryset


