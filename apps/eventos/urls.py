from django.urls import path
from .views import (
    listar_eventos, 
    crear_evento, 
    detalle_evento,
    modificar_evento,
    eliminar_evento
    )

urlpatterns = [
    # www.mipagina.com/eventos/
    path('', listar_eventos, name="inicio"),

    # www.mipagina.com/eventos/crear
    path('crear/', crear_evento, name="crear_evento"),

    # www.mipagina.com/eventos/{UN_ID}
    path('un_evento/', detalle_evento, name="detalle_evento"),

    # www.mipagina.com/eventos/modificar/{UN_ID}
    path('modificar/', modificar_evento, name="modificar_evento"),

    # www.mipagina.com/eventos/eliminar/{UN_ID}
    path('eliminar/', eliminar_evento, name="eliminar_evento"),
]
