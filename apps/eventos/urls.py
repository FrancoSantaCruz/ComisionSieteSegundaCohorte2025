from django.urls import path
from .views import listar_eventos

urlpatterns = [
    # www.mipagina.com/eventos/
    path('', listar_eventos, name="inicio"),

    # www.mipagina.com/eventos/{UN_ID}
    # path('{UN_ID}/', detalle_un_evento, name="inicio"),

    # www.mipagina.com/eventos/crear
    # path('crear/', crear_evento, name="inicio"),

    # www.mipagina.com/eventos/modificar/{UN_ID}
    # path('modificar/{UN_ID}/', modificar_evento, name="inicio"),

    # www.mipagina.com/eventos/eliminar/{UN_ID}
    # path('eliminar/{UN_ID}/', eliminar_evento, name="inicio"),
]
