from django.urls import path

from .views import AgendamentoCreate


urlpatterns = [
    path('agendar/', AgendamentoCreate.as_view(), name="agendamento"),
]