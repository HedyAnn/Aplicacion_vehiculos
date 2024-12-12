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