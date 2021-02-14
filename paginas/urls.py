from django.urls import path

from servicos.views import SalaoList
from .views import PaginaInicial

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),


]
