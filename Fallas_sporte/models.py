from django.db import models
from Maestro.models import *
from Anexos.models import *
from .choices import *
# Create your models here.

class Falla(models.Model):
    salas = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True, blank=True)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, null=True, blank=True)
    #fecha_instalacion = models.ForeignKey(Maquina, on_delete=models.CASCADE, null=True, blank=True)
    id_error = models.ForeignKey(CodigoFalla, on_delete=models.CASCADE, null=True, blank=True)
    id_causa = models.ForeignKey(CausasFalla, on_delete=models.CASCADE, null=True, blank=True)
    id_solucion = models.ForeignKey(SolucionFalla, on_delete=models.CASCADE, null=True, blank=True)
    numero = models.CharField(max_length=20)
    reportado = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    descripcion_igg = models.CharField(max_length=100)
    apagada = models.IntegerField(default=0)
    fecha = models.DateTimeField(null=True)
    fecha_solucion = models.DateTimeField(null=True)
    id_status = models.IntegerField(default=0, choices=Status)
    observacion = models.CharField(max_length=100)
    eliminar = models.IntegerField(default=0)
    email = models.IntegerField(default=0)
    email_igg = models.IntegerField(default=0)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, null=True, blank=True)
    id_seguridad = models.IntegerField(default=0)
    fecha_seguridad = models.DateTimeField(null=True)
    sincroniza = models.IntegerField(default=0)
    fecha_sincroniza = models.DateTimeField()
    telefono = models.CharField(max_length=50)
    prioridad = models.IntegerField(default=50, choices=prioridad)
    atencion = models.IntegerField(default=50, choices=atencion)
    resuelto = models.CharField(max_length=50, choices=resuelto)
    fecha_parcial = models.DateTimeField()
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, null=True, blank=True)
    fecha_atencion = models.DateTimeField(null=True)
    fecha_reopen = models.DateTimeField(null=True)
    fecha_escalado = models.DateTimeField(null=True)
    email_igg2 = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

class ServicioTecnico(models.Model):
    numero = models.CharField(max_length=20)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    partes = models.CharField(max_length=100)
    id_status = models.IntegerField(default=50, choices=StatusServicioTecnico)
    fecha = models.DateTimeField()
    fecha_visita = models.DateTimeField()
    fecha_final = models.DateTimeField()
    observacion = models.IntegerField(default=0)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, null=True, blank=True)
    eliminar = models.IntegerField(default=0)
    id_falla = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

class Remisiones(models.Model):
    numero = models.CharField(max_length=20)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    contacto = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    id_status = models.IntegerField(default=50, choices=StatusRemision)
    fecha = models.DateTimeField()
    fecha_envio = models.DateTimeField()
    fecha_recibido = models.DateTimeField()
    guia = models.CharField(max_length=30)
    id_transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, null=True, blank=True)
    observacion = models.CharField(max_length=100)
    eliminar = models.IntegerField(default=0)
    elaborado = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

class Reparaciones(models.Model):
    numero = models.CharField(max_length=20)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    id_status = models.IntegerField(default=50, choices=StatusSReparacion)
    fecha = models.DateTimeField()
    fecha_recibido = models.DateTimeField()
    fecha_final = models.DateTimeField()
    observacion = models.CharField(max_length=100)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, null=True, blank=True)
    eliminar = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")


