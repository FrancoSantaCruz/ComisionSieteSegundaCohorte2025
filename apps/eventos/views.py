from django.shortcuts import render
from .models import Evento, Categoria, Organizador

# Create your views here. Obligame

## CRUD
### C.CREATE
def crear_evento(request):
    # Como recibir información desde el front
    organizador_ejemplo = Organizador.objects.create(nombre="Roman Huel", correo="hroman@example.com")

    # categoria_uno = Categoria.objects.create(nombre="Tecnología", descripcion="Eventos tech")
    # categoria_dos = Categoria.objects.create(nombre="Innovación", descripcion="Novedades del sector")

    categoria_dos = Categoria.objects.get(categoria_id=2)

    evento = Evento(
        titulo = "Expo Agrimensura 2026",
        descripcion = "Exposición agrimensura 2026",
        fecha_inicio = "2026-12-01",
        hora_inicio = "18:00:00",
        hora_fin = "22:00:00",
        direccion = "Av. Lavalle 123",
        es_gratuito = False,
        precio = 8000,
        organizador = organizador_ejemplo,
    )

    evento.save()

    evento.categoria.add(categoria_dos)

    print("Se crearon los registros correctamente.")

    #Como enviar el resultado al HTML y mostrarlo en el HTML. 
    return render(request, 'crear_evento.html')

### R.READ
def listar_eventos(request):
    todos_los_eventos = Evento.objects.all()
    print(todos_los_eventos)

    eventos_filtrados = Evento.objects.filter(titulo="Expo Agrimensura 2026")

    print(eventos_filtrados)

    return render(request, 'todos_los_eventos.html')

def detalle_evento(request):
    un_evento = Evento.objects.get(evento_id=1)
    print(un_evento.evento_id)
    print(un_evento.titulo)
    print(un_evento.descripcion)
    print(un_evento.direccion)
    return render(request, 'detalle_evento.html')

def modificar_evento(request):
    # ID el evento
    id_recibido = 2
    # Los datos a modificar
    titulo_recibido = "Expo Carpinteria 2026"
    direccion_recibido = "Av. Castelli 1100"

    evento_a_modificar = Evento.objects.get(evento_id=id_recibido)

    evento_a_modificar.titulo = titulo_recibido
    evento_a_modificar.direccion = direccion_recibido

    evento_a_modificar.save()

    return render(request, 'modificar_evento.html')

def eliminar_evento(request):
    id_recibido = 2

    evento_a_eliminar = Evento.objects.get(evento_id=id_recibido)
    
    evento_a_eliminar.delete()

    return render(request, 'eliminar_evento.html')