from django.urls import path

from .views import AgendamentoCreate
from .views import AgendamentoList


urlpatterns = [
    path('agendar/<int:pk>', AgendamentoCreate.as_view(), name="agendamento"),
    path('listarAgendamentos/', AgendamentoList.as_view(), name="listarAgendamentos"),
]