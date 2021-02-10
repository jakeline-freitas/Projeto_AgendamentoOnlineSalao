from django.urls import path

from .views import AgendamentoCreate
from .views import AgendamentoList


urlpatterns = [
    path('agendar/', AgendamentoCreate.as_view(), name="agendamento"),
    #path('listarAgendamentos/<int:pk>', AgendamentoList.as_view(), name="listarAgendamentos"),
    path('listarAgendamentos/', AgendamentoList.as_view(), name="listarAgendamentos"),
]