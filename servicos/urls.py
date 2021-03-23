from django.urls import path

from .views import SalaoCreate, SalaoList, ServicoList, SaloesDetail, SalaoListUser
from .views import ServicosCreate, ServicosUpdate, SalaoUpdate
from .views import ServicosDelete, SalaoDelete

urlpatterns = [
    path('cadastrarServico/', ServicosCreate.as_view(), name="cadastrarServico"),
    path('cadastrarSalao/', SalaoCreate.as_view(), name="cadastrarSalao"),

    path('editarServico/<int:pk>/', ServicosUpdate.as_view(), name="editarServico"),
    path('editarSalao/<int:pk>/', SalaoUpdate.as_view(), name="editarSalao"),

    path('excluirServico/<int:pk>/', ServicosDelete.as_view(), name="excluirServico"),
    path('editarSalao/<int:pk>/', SalaoDelete.as_view(), name="excluirSalao"),

    path('listarSaloes/', SalaoList.as_view(), name="listarSaloes"),
    path('listarSaloesUser/', SalaoListUser.as_view(), name="listarSaloesUser"),
    path('listarServicos/', ServicoList.as_view(), name="listarServicos"),

    path('listarServicosId/<int:pk>', ServicoList.as_view(), name="listarServicosId"),
    path('detalhesSalaoId/<int:pk>', SaloesDetail.as_view(), name="detalhesSalao"),
]
