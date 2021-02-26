from django import forms
from django.forms import ModelForm

from .models import Agendamento
from .models import Servico


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'


class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'hora', 'tempo']
        widgets = {
            'data': DateInput(),
            'hora': TimeInput(),
            'tempo': TimeInput(),
        }

    servico = forms.ModelMultipleChoiceField(
        queryset=Servico.Servicos.all(),
        widget=forms.CheckboxSelectMultiple
    )
