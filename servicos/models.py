from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Salao(models.Model):
    nome = models.CharField(max_length=255)
    localizacao = models.TextField(verbose_name='Localização')
    responsavel = models.ForeignKey('accounts.User', verbose_name='Responsáveis',on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estabelecimento = models.ForeignKey(Salao, verbose_name='Salão de beleza', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "servico"
        verbose_name_plural = "serviços"

    def __str__(self):
        return self.nome