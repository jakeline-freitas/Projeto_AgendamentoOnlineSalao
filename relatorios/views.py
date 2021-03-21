from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import View, CreateView, FormView
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


class GeneratePdf(CreateView, GroupRequiredMixin, LoginRequiredMixin):
    group_required = u"Proprietários"
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        hoje = datetime.today()
        user = self.request.user
        age = Agendamento.objects.filter(data=hoje)
        saloes = [salao.id for salao in Salao.objects.filter(responsavel=self.request.user)]
        servicos = [servico.id for servico in Servico.Servicos.filter(estabelecimento__in=saloes)]
        agendamentos = AgendamentoServico.objects.filter(agendamento__in=age, servico__in=servicos)
        data = {'age': agendamentos,
                'data_i': hoje,
                'data_f':hoje,
                'u':user}
        pdf = render_to_pdf('relatorios/relatorio_dia.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePdfIntervalo(View):

    def get(self, request, *args, **kwargs):
        data = {'form': RelatorioForm()}
        return render(request, 'relatorios/relatorio_intervalo.html', data)

    def post(self, request):
        form = RelatorioForm(data=request.POST)
        if form.is_valid():
            user = self.request.user
            data_inicio = form.cleaned_data.get('data_inicio')
            data_fim = form.cleaned_data.get('data_fim')

            age = Agendamento.objects.filter(data__range=[data_inicio, data_fim])
            saloes = [salao.id for salao in Salao.objects.filter(responsavel=self.request.user)]
            servicos = [servico.id for servico in Servico.Servicos.filter(estabelecimento__in=saloes)]
            agendamentos = AgendamentoServico.objects.filter(agendamento__in=age, servico__in=servicos)
            data = {'age': agendamentos,
                    'data_i': data_inicio,
                    'data_f': data_fim,
                    'u': user}
            pdf = render_to_pdf('relatorios/relatorio_dia.html', data)
            return HttpResponse(pdf, content_type='application/pdf')

        return HttpResponseRedirect("/relatorios/gerar_relatorio_intervalo/")