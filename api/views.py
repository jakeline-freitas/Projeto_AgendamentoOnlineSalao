from rest_framework import viewsets

from agendamento.models import Agendamento
from servicos.models import Servico, Salao
from accounts.models import User
from api.serializers import ServicoSerializer, SalaoSerializer, AgendamentoSerializer, UserSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.Servicos.all()
    serializer_class = ServicoSerializer


class SalaoViewSet(viewsets.ModelViewSet):
    queryset = Salao.objects.all()
    serializer_class = SalaoSerializer


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
