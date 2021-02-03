from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from servicos.models import Servico


class Agendamento(TimeStampedModel):
    ESTADOS = (
        ('A', 'Agendado'),
        ('E', 'Esperando'),
        ('C', 'Cancelado')
    )
    data = models.DateField()
    hora = models.TimeField()
    tempo = models.TimeField()
    estado = models.CharField(max_length=1, choices=ESTADOS, default='E')
    servico = models.ForeignKey(Servico, verbose_name='Serviço', on_delete=models.CASCADE)
    cliente = models.ForeignKey('accounts.User', verbose_name='Cliente', on_delete=models.CASCADE)

    class Meta:
        ordering = ("data",)
