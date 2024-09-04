from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View

from django.db.models.functions import TruncMonth
from django.urls import reverse_lazy

from .models import Evento

class EventosPorMesView(ListView):
    model = Evento
    template_name = 'lista/eventos_por_mes.html'
    context_object_name = 'eventos'
    def get(self, request, *args, **kwargs):
        if 'nome_usuario' not in request.session:
            return redirect('lista_section')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Evento.objects.annotate(mes=TruncMonth('data')).values('mes').annotate(total=Count('id')).order_by('mes')
    

class EventosDoMesView(ListView):
    model = Evento
    template_name = 'lista/eventos_do_mes.html'
    context_object_name = 'eventos'

    def get(self, request, *args, **kwargs):
        if 'nome_usuario' not in request.session:
            return redirect('lista_section')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        ano = self.kwargs['ano']
        mes = self.kwargs['mes']
        return Evento.objects.filter(data__month=mes, data__year=ano).order_by('data')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ano'] = self.kwargs['ano']
        context['mes'] = self.kwargs['mes']
        return context
    

class EventosCreateView(CreateView):
    model = Evento

    def get(self, request, *args, **kwargs):
        if 'nome_usuario' not in request.session:
            return redirect('lista_section')
        return super().get(request, *args, **kwargs)

    fields = ["nome", "data", "hora", "numero_convidados", "local"]
    success_url = reverse_lazy('eventos_por_mes')

#Classe para editar os eventos
class EventosUpdateView(UpdateView):
    model = Evento

    def get(self, request, *args, **kwargs):
        if 'nome_usuario' not in request.session:
            return redirect('lista_section')
        return super().get(request, *args, **kwargs)

    fields = ["nome", "data", "hora", "numero_convidados", "local"]
    template_name = "lista/evento_form.html"
    success_url = reverse_lazy('eventos_por_mes')

#Classe para deletar os eventos
class EventosDeleteView(DeleteView):
    model = Evento

    def get(self, request, *args, **kwargs):
        if 'nome_usuario' not in request.session:
            return redirect('lista_section')
        return super().get(request, *args, **kwargs)

    template_name = "lista/eventos_delete.html"
    success_url = reverse_lazy('eventos_por_mes')

class SolicitarDadosView(View):

    def get(self, request):
        return render(request, 'section/section.html')

    def post(self, request):
        nome_usuario = request.POST.get('nome_usuario')
        email = request.POST.get('email')

        #Armazenando os dados na sessão
        request.session['nome_usuario'] = nome_usuario
        request.session['email'] = email

        return redirect('eventos_por_mes')

class EncerrarSessaoView(View):
    def get(self, request):
        request.session.flush()
        return redirect('/')