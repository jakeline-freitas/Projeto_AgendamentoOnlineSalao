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
    tempo = models.TimeField(verbose_name='tempo gasto no atendimento')
    estado = models.CharField(max_length=1, choices=ESTADOS, default='E')
    servico = models.ManyToManyField(Servico, through="AgendamentoServico")
    cliente = models.ForeignKey('accounts.User', verbose_name='Cliente', on_delete=models.CASCADE)
    totalAPagar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='preçoTotal')

    class Meta:
        ordering = ("data",)

    def __str__(self):
        return "{} - {}".format(self.data, self.cliente.email)


class AgendamentoServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name="servicoAgendam")
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, related_name="servicoAgendam")
