from django.shortcuts import render
from apps.eventos.models import Evento

def inicio(request):
    return render(request, 'inicio.html')
# def inicio(request):
#     eventos = Evento.objects.all()
#     return render(request, 'index.html', {'eventos': eventos})