from django.forms import ModelForm

from .models import Servico, Salao


class SalaoForm(ModelForm):
    class Meta:
        model = Salao
        fields = "__all__"


class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = "__all__"