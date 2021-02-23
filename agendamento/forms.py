from django.forms import ModelForm
from django import forms

from servicos.models import Salao
from .models import Servico
from .models import Agendamento


class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'hora', 'tempoASerGasto', 'servico', ]

    servico = forms.ModelMultipleChoiceField(
        queryset=Servico.Servicos.all(),
        widget=forms.CheckboxSelectMultiple
    )

