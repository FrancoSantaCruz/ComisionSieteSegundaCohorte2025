from django.urls import path
from .views import (
    registrar_usuario,
    ingresar_usuario,
    cerrar_sesion
    )

app_name = "apps.autenticacion"

urlpatterns = [
    path('registrar/', registrar_usuario, name='registrar'),
    path('ingresar/', ingresar_usuario, name='ingresar'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
]
