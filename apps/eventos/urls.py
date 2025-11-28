from django.urls import path
from .views import (
    listar_eventos, 
    crear_evento, 
    detalle_evento,
    modificar_evento,
    eliminar_evento,

    ListarEventosView,
    DetalleEventoView,
    CrearEventoView,
    ModificarEventoView,
    EliminarEventoView
    )

urlpatterns = [

    # http://localhost:8000/eventos/
    #FBV
    path('', listar_eventos, name="listar_eventos"),
    #CBV
    # path('', ListarEventosView.as_view(), name="listar_eventos"),

    # http://localhost:8000/eventos/crear
    #FBV
    path('crear/', crear_evento, name="crear_evento"),
    #CBV
    # path('crear/', CrearEventoView.as_view(), name="crear_evento"),

    # http://localhost:8000/eventos/un_evento/1
    #FBV
    path('un_evento/<int:pk>', detalle_evento, name="detalle_evento"),
    #CBV
    # path('un_evento/<int:pk>', DetalleEventoView.as_view(), name="detalle_evento"),

    # http://localhost:8000/eventos/modificar/1
    #FBV
    path('modificar/<int:pk>', modificar_evento, name="modificar_evento"),
    #CBV
    # path('modificar/<int:pk>', ModificarEventoView.as_view(), name="modificar_evento"),

    # http://localhost:8000/eventos/eliminar/1
    #FBV
    path('eliminar/<int:pk>', eliminar_evento, name="eliminar_evento"),
    #CBV
    # path('eliminar/<int:pk>', EliminarEventoView.as_view(), name="eliminar_evento"),
]
