from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        # fields = '__all__'
        fields = [
            'titulo', 
            'descripcion',
            'categoria',
            'fecha_inicio',
            'hora_inicio',
            'hora_fin',
            'es_gratuito',
            'precio',
            'direccion',
            'organizador'
            ]
        widgets = {
            'fecha_inicio': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'hora_inicio': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),
            'hora_fin': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            )
        }
