from django.urls import path

from .views import ServicosCreate, SalaoCreate
from .views import ServicosUpdate, SalaoUpdate
from .views import ServicosDelete, SalaoDelete


urlpatterns = [
    path('cadastrarServico/', ServicosCreate.as_view(), name="cadastrarServico"),
    path('cadastrarSalao/', SalaoCreate.as_view(), name="cadastrarSalao"),

    path('editarServico/<int:pk>/', ServicosUpdate.as_view(), name="editarServico"),
    path('editarSalao/<int:pk>/', SalaoUpdate.as_view(), name="editarSalao"),

    path('excluirServico/<int:pk>/', ServicosDelete.as_view(), name="excluirServico"),
    path('editarSalao/<int:pk>/', SalaoDelete.as_view(), name="excluirSalao"),
]