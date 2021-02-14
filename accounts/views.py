from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from .models import User


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Clientes")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context
