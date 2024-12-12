from django.shortcuts import render
from . form import VehiculoForm
from . models import Vehiculo
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def agregar_vehiculo(request):
    return render(request, 'add.html')

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'add.html'
    success_url = reverse_lazy('index.html')

def index(request):  # Antes: home
    return render(request, 'index.html')

@login_required
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listar.html', {'vehiculos': vehiculos})

@login_required
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    vehiculos_con_condicion = []
    for vehiculo in vehiculos:
        if vehiculo.precio < 10000:
            condicion_precio = 'Bajo'
        elif 10000 <= vehiculo.precio <= 30000:
            condicion_precio = 'Medio'
        else:
            condicion_precio = 'Alto'

        vehiculos_con_condicion.append({
            'vehiculo': vehiculo,
            'condicion_precio': condicion_precio
        })
    
    context = {'vehiculos_con_condicion': vehiculos_con_condicion}
    return render(request, 'listar.html', context)