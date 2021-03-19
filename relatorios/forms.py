from django import forms


class RelatorioForm(forms.Form):
    #saloes = forms.ModelChoiceField(required=True)
    data_inicio = forms.DateField(required=True)
    data_fim = forms.DateField(required=True)
