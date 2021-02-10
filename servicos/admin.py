from django.contrib import admin
from .models import Salao, Servico


@admin.register(Salao)
class SalaoAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "localizacao",
        "responsavel",

    ]


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "preco",
        "estabelecimento",

    ]
