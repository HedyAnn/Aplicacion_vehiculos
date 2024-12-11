from django.db import models

# Create your models here.

marcas = (('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota'))

categoria = (('particular', 'Particular'), ('carga', 'Carga'), ('transporte', 'Transporte'), ('carga', 'Carga'))

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20,choices=marcas)
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    serialCarroceria = models.CharField(max_length=50)
    serialMotor = models.CharField(max_length=50, verbose_name='Serial Motor')
    categoria = models.CharField(max_length=20, choices=categoria)
    precio = models.IntegerField()
    fechaCreacion = models.DateField(auto_now_add=True)
    fechaModificacion = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.serialCarroceria}'
    