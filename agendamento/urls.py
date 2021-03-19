from django.urls import path

from .views import AgendamentoCreate, AgendamentoServicoUpdate
from .views import AgendamentoList
from .views import TodosAgendamentosList

urlpatterns = [
    path('agendar/<int:pk>', AgendamentoCreate.as_view(), name="agendamento"),
    path('listarAgendamentos/', AgendamentoList.as_view(), name="listarAgendamentos"),
    path('listarTodosAgendamentos/', TodosAgendamentosList.as_view(), name="listarTodosAgendamentos"),
    path('confirmarAgendamento/<int:pk>/', AgendamentoServicoUpdate.as_view(), name='updateAgendamento'),
]
