from django.urls import include, path
from api.views import ServicoViewSet, SalaoViewSet, AgendamentoViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'servicos', ServicoViewSet)
router.register(r'saloes', SalaoViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'usuarios', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
