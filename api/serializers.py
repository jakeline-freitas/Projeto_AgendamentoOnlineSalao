from rest_framework import serializers

from agendamento.models import Agendamento
from servicos.models import Servico, Salao
from accounts.models import User


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['data', 'hora', 'estado', 'totalAPagar', 'cliente']


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['nome', 'preco', 'estabelecimento']


class SalaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salao
        fields = ['nome', 'localizacao', 'responsavel', 'image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']