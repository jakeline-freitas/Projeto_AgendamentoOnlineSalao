from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import ServicoForm
from .models import Servico, Salao
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


####### Create #########


class ServicosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Servico
    group_required = u"Proprietários"
    fields = '__all__'
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(ServicosCreate, self).get_context_data(**kwargs)
        #estabelecimento = Salao.objects.filter(responsavel= self.request.user)
        #estabelecimentos = [estabelecimento for estabelecimento in Salao.objects.filter(responsavel=self.request.user)]
        context['form'].fields['estabelecimento'].queryset = Salao.objects.filter(responsavel=self.request.user)
        return context


class SalaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Salao
    group_required = [u"Proprietários", u"Adminstrador"]
    fields = ['nome', 'image', 'localizacao']
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.responsavel = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


###### Update ######


class ServicosUpdate(LoginRequiredMixin, UpdateView):
    model = Servico
    form_class = ServicoForm
    # fields = ['preco', 'descricao', 'is_available']
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')


class SalaoUpdate(LoginRequiredMixin, UpdateView):
    model = Salao
    fields = ['nome', 'image', 'localizacao']
    template_name = 'servicos/formularioCreate.html'
    success_url = reverse_lazy('index')


####### Delete #########


class ServicosDelete(LoginRequiredMixin, DeleteView):
    model = Servico
    template_name = 'servicos/formularioDelete.html'
    success_url = reverse_lazy('index')


class SalaoDelete(LoginRequiredMixin, DeleteView):
    model = Salao
    template_name = 'servicos/formularioDelete.html'
    success_url = reverse_lazy('listarSaloes')


####### List #########


class SalaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    paginate_by = 6
    model = Salao
    template_name = 'servicos/listarSaloes.html'

    def get_queryset(self):
        return Salao.objects.all().order_by('nome')


class SalaoListUser(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Salao
    template_name = 'servicos/listarSaloesTabela.html'

    def get_queryset(self):
        queryset = Salao.objects.filter(responsavel=self.request.user).order_by('nome')
        return queryset


class ServicoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Servico
    template_name = 'servicos/listarServicos.html'

    def get_queryset(self):
        queryset = Servico.available.all()
        salao = Salao.objects.filter(responsavel=self.request.user)

        queryset = queryset.filter(estabelecimento__in=salao)
        return queryset


####### Detail #########


class SaloesDetail(DetailView):
    queryset = Salao.objects.all()
    template_name = 'servicos/listarSaloesTabela.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SaloesDetail, self).get_context_data(*args, **kwargs)
        return context
