from .models import Documento
from django.views.generic import CreateView

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def form_valid(self, form):
        form.instance.pertence_id = self.kwargs['funcionario_id']
        return super().form_valid(form)