from relatorios.views import GeneratePdf
from django.urls import path
urlpatterns = [

    path("relatorio/gerar", GeneratePdf.as_view(), name="gerar_relatorio"),

]