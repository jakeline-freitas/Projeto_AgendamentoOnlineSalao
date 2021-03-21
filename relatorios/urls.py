from relatorios.views import GeneratePdf, GeneratePdfIntervalo
from django.urls import path

urlpatterns = [

    path("relatorio/gerar", GeneratePdf.as_view(), name="gerar_relatorio"),
    path("relatorio_intervalo/gerar", GeneratePdfIntervalo.as_view(), name="gerar_relatorio_intervalo"),

]
