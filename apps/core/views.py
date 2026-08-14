from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario

@login_required #isso faz essa pagina só poder ser acessada por usuarios q fizeram login
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html',data)
