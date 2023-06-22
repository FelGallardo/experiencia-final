import os
from django.shortcuts import render, redirect
from django.urls import path
from django.shortcuts import render
from .forms import RegistroUserForm, ProductoForm
from .models import Productos
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def producto(request):
    plantas = Productos.objects.all()
    datos={
        'plantas':plantas
    }
    return render(request, 'producto.html',datos)

def nosotros(request):
    return render(request, 'nosotros.html')

def Api(request):
    return render(request, 'Api.html')

def registrar(request):
    data ={
        'form':RegistroUserForm()
    }
    if request.method == "POST":
        formulario = RegistroUserForm(data = request.POST)
        if formulario.is_valid:
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('index')
        data['form'] = formulario
    return render (request, 'registration/registrar.html', data)


@login_required
def crear(request):
    if request.method=="POST":
        productoform= ProductoForm(request.POST,request.FILES)
        if productoform.is_valid():
            productoform.save()
            return redirect ('producto')
    else:
        productoform=ProductoForm()
    return render (request, 'crear.html', {'productoform':productoform})

@login_required
def eliminar(request, id):
    productoEliminado = Productos.objects.get(idprod=id)
    productoEliminado.delete()
    return redirect ('producto')

@login_required
def modificar(request, id):
    productoModifi = Productos.objects.get(idprod=id)
    datos={
        'form':ProductoForm(instance=productoModifi)
    }
    
    if request.method=="POST":
        if len(request.FILES) !=0:
            if productoModifi.imagen:
                os.remove(productoModifi.imagen.path) 
            productoModifi.imagen = request.FILES['imagen']
        formulario= ProductoForm(data=request.POST, instance=productoModifi)
        if formulario.is_valid():
            formulario.save()
            return redirect('producto')
    return render(request, 'modificar.html', datos)