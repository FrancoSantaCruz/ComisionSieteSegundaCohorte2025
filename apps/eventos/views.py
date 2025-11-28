from django.shortcuts import render
from .models import Evento, Categoria, Organizador

from .forms import EventoForm
from django.shortcuts import redirect

##########
## CRUD ##
##########

### FBV (Vistas Basadas en Funciones)
# READ - GET
def listar_eventos(request):
    todos_los_eventos = Evento.objects.all()
    todas_las_categorias = Categoria.objects.all()
    contexto = {
        'eventos': todos_los_eventos,
        'categorias': todas_las_categorias
    }
    return render(request, 'todos_los_eventos.html', contexto)

def detalle_evento(request, pk):
    try:
        un_evento = Evento.objects.get(evento_id=pk)

        contexto = {
            'evento': un_evento
        }

        return render(request, 'detalle_evento.html', contexto)
    except Evento.DoesNotExist:
        contexto = {
            'evento': None
        }
        return render(request, 'detalle_evento.html', contexto)

# CREATE - GET / POST
def crear_evento(request):
    if request.method == 'POST':
        # POST -> Recibiendo información mediante un formulario
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        # GET -> Tengo que mostrar el formulario vacío
        form = EventoForm()
    
    return render(request, 'crear_evento.html', {'form': form})
    
# UPDATE - GET / POST
def modificar_evento(request, pk):
    evento_a_modificar = Evento.objects.get(evento_id=pk)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento_a_modificar)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento_a_modificar)

    return render(request, 'modificar_evento.html', {'form': form })

# DELETE - GET / POST
def eliminar_evento(request, pk):
    evento_a_eliminar = Evento.objects.get(evento_id=pk)

    if request.method == 'POST':
        evento_a_eliminar.delete()
        return redirect('listar_eventos')

    return render(request, 'eliminar_evento.html', {'evento': evento_a_eliminar})


### CBV (Vistas Basadas en Clases)

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ListarEventosView(ListView):
    model = Evento
    template_name = 'todos_los_eventos.html'
    context_object_name = "eventos"

class DetalleEventoView(DetailView):
    model = Evento
    template_name = 'detalle_evento.html'
    context_object_name = "evento"

class CrearEventoView(CreateView):
    model = Evento
    template_name = 'crear_evento.html'
    form_class = EventoForm
    success_url = reverse_lazy('listar_eventos')

class ModificarEventoView(UpdateView):
    model = Evento
    template_name = 'modificar_evento.html'
    form_class = EventoForm
    success_url = reverse_lazy('listar_eventos')

class EliminarEventoView(DeleteView):
    model = Evento
    template_name = 'eliminar_evento.html'
    success_url = reverse_lazy('listar_eventos')
