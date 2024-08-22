from django.shortcuts import render
from .models import Evento
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models.functions import TruncMonth
from django.db.models import Count

# Create your views here.

def sobre(request):
    mensagem = 'Agenda de Eventos'
    contexto = {
        'titulo': mensagem
    }
    return render(request, 'lista/sobre.html', contexto)


class EventoListView(ListView):
    model = Evento
    def get_queryset(self):
        queryset = Evento.objects.annotate(
            mes = TruncMonth('data')
        ).values('mes').annotate(total=Count('id')).order_by('mes')
        return queryset

class EventoCreate(CreateView):
    # Informa o modelo a ser usado
    model = Evento

    #Quais comapos da nossa tabela será preenchida
    fields = ['nome', 'data', 'hora', 'numero_convidados', 'local']

    # Redireciona para uma página
    success_url = reverse_lazy('evento_list')