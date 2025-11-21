from django.shortcuts import render

# Create your views here. Obligame

def listar_eventos(request):
    return render(request, 'todos_los_eventos.html')