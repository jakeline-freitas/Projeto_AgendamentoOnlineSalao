from django.contrib import admin
from .models import Agendamento, AgendamentoServico


class AgendamentoServicoInline(admin.TabularInline):
    model = AgendamentoServico


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = [
        "data",
        "hora",
        "cliente",
    ]

    inlines = (AgendamentoServicoInline,)








