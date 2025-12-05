from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrarUsuarioForm, IngresarUsuarioForm

# Create your views here.

def registrar_usuario(request):
    if request.method == 'POST':
        #POST
        form = RegistrarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('apps.autenticacion:ingresar')
    else:
        #GET
        form = RegistrarUsuarioForm()
    
    return render(request, 'autenticacion/registrar.html', {'form': form})


def ingresar_usuario(request):
    if request.method == 'POST':
        #POST
        form = IngresarUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, intentalo de nuevo')
    else:
        form = IngresarUsuarioForm()

    return render(request, 'autenticacion/ingresar.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('apps.autenticacion:ingresar')


# FBV -> Decorators -> Decoradores

# CBV -> Mixins