from django.views.generic import ListView, CreateView
from django.db.models import Count

from django.db.models.functions import TruncMonth
from django.urls import reverse_lazy

from .models import Evento

class EventosPorMesView(ListView):
    model = Evento
    template_name = 'lista/eventos_por_mes.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        return Evento.objects.annotate(mes=TruncMonth('data')).values('mes').annotate(total=Count('id')).order_by('mes')
    

class EventosDoMesView(ListView):
    model = Evento
    template_name = 'lista/eventos_do_mes.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        return Evento.objects.filter(data__year=ano, data__month=mes).order_by('data')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ano'] = self.kwargs['ano']
        context['mes'] = self.kwargs['mes']
        return context
    

class EventosCreateView(CreateView):
    model = Evento
    fields = ["nome", "data", "hora", "numero_convidados", "local"]
    success_url = reverse_lazy('eventos_por_mes')