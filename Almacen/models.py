from django.db import models
from Maestro.models import *
from Anexos.models import *
from .choices import *

# Create your models here.
class Importaciones(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

class Declaracione(models.Model):
    numero = models.CharField(max_length=20)
    proveedor = models.ForeignKey(Proveedore, on_delete=models.CASCADE, null=True, blank=True)
    id_status = models.IntegerField(default=0)
    id_ano = models.IntegerField(default=0)
    fecha = models.DateTimeField()
    fecha_factura = models.DateTimeField()
    fecha_recibido = models.DateTimeField()
    observacion = models.CharField(max_length=100)
    eliminar = models.IntegerField()
    id_seguridad = models.IntegerField(default=0)
    fecha_seguridad = models.DateTimeField()
    factura = models.CharField(max_length=20)
    referencia = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

class Inventario(models.Model):
    numero = models.CharField(max_length=20)
    id_declaracion = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, null=True)
    id_status = models.IntegerField(default=50, choices=Status)
    estado = models.IntegerField(default=50, choices=Estado)
    fecha_despacho = models.DateTimeField()
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    fecha_ingreso = models.DateTimeField()
    serial = models.CharField(max_length=30)
    piezas = models.ForeignKey(Pieza, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

