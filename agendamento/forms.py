from django.forms import ModelForm
from django import forms

from Utils.widgets import BootstrapDateTimePickerInput
from .models import Servico
from .models import Agendamento


class AgendamentoForm(ModelForm):
    data = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )
    #data = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Agendamento
        fields = ['data', 'hora', 'tempo', ]

    servico = forms.ModelMultipleChoiceField(
        queryset=Servico.Servicos.all(),
        widget=forms.CheckboxSelectMultiple
    )


