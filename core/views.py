from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# def agenda(request, titulo_evento):
#     titulo = titulo_evento
#     return HttpResponse('<h1>O evento é {}, no local {}</h1>'.format(titulo_evento, titulo_evento))

def index(request):
    return redirect('/agenda/')

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
# Create your views here.
