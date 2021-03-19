from datetime import datetime

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from xhtml2pdf import pisa

from agendamento.models import Agendamento, AgendamentoServico
from servicos.models import Salao, Servico
from .forms import RelatorioForm
from io import BytesIO


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        hoje = datetime.today()

        age = Agendamento.objects.filter(data=hoje)
        saloes = [salao.id for salao in Salao.objects.filter(responsavel=self.request.user)]
        servicos = [servico.id for servico in Servico.Servicos.filter(estabelecimento__in=saloes)]
        agendamentos = AgendamentoServico.objects.filter(agendamento__in=age, servico__in=servicos)
        data = {'age': agendamentos}
        pdf = render_to_pdf('relatorios/relatorio_dia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

