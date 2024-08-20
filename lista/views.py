from django.shortcuts import render
from .models import Evento

from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


# Create your views here.

def sobre(request):
    mensagem = 'Agenda de Eventos'
    contexto = {
        'titulo': mensagem
    }
    return render(request, 'lista/sobre.html', contexto)


class EventoListView(ListView):
    model = Evento


class EventoCreate(CreateView):
    # Informa o modelo a ser usado
    model = Evento

    #QQuais comapos da nossa tabela será preenchida
    fields = ['nome', 'data', 'hora', 'numero_convidados', 'local']

    # Redireciona para uma página
    success_url = reverse_lazy('evento_list')
