from django.urls import path

from .views import AgendamentoListView

app_name = "agendamento"

urlpatterns = [
    path("", AgendamentoListView.as_view(), name="list"),
]