from django.db import models
from autoslug import AutoSlugField


class Salao(models.Model):
    nome = models.CharField(max_length=255)
    image = models.ImageField(upload_to="saloes/%Y/%m/%d", blank=True)
    localizacao = models.TextField(verbose_name='Localização')
    responsavel = models.ForeignKey('accounts.User', verbose_name='Responsáveis', on_delete=models.CASCADE)

    saloes = models.Manager()

    class Meta:
        verbose_name = "salão"
        verbose_name_plural = "salões"

    def __str__(self):
        return self.nome


class AvailableManager(models.Manager):  # personalizando novo manager
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)  # filtro para serviços disponiveis


class Servico(models.Model):
    nome = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='preço')
    estabelecimento = models.ForeignKey(Salao, on_delete=models.CASCADE)
    descricao  = models.TextField(blank=True, verbose_name='descrição')
    is_available = models.BooleanField(default=True)

    Servicos = models.Manager()  # manager padrão
    available = AvailableManager()  # novo manager

    class Meta:
        verbose_name = "servico"
        verbose_name_plural = "serviços"

    def __str__(self):
        return self.nome
