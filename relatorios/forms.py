from django import forms

from servicos.models import Salao


class RelatorioForm(forms.Form):
    data_inicio = forms.DateField(required=True)
    data_fim = forms.DateField(required=True)
