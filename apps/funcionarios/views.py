from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):#filtrando os funcionarios de acordo com a empresa do usuario logado
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ('nome', 'departamentos')

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ('nome', 'departamentos')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['nome'].widget.attrs['placeholder'] = 'Nome e sobrenome'

        return form

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username =funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)
                                            