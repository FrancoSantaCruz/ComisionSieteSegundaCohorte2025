from django.contrib import admin
from .models import Evento, Categoria, Organizador

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    fields = ('titulo', 'descripcion', 'categoria', 'fecha_inicio', 'hora_inicio', 'hora_fin', 'direccion')

    list_display = ('titulo', 'fecha_inicio')

    search_fields = ('titulo',)

    list_filter = ('fecha_inicio',)


admin.site.register(Organizador)
admin.site.register(Categoria)
admin.site.register(Evento, EventoAdmin)