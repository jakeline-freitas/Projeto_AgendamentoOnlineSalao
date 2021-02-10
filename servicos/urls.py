from django.urls import path

from .views import ServicosCreate, SalaoCreate


urlpatterns = [
    path('cadastrarServico/', ServicosCreate.as_view(), name="cadastrarServico"),
    path('cadastrarSalao/', SalaoCreate.as_view(), name="cadastrarSalao"),
]