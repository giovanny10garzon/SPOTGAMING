from django.db import models
from .choices import *
from Anexos.models import *
from Maestro.models import *

# Create your models here.
class Contrato(models.Model):
    id_status = models.IntegerField(choices=Status_Contrato)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    razon = models.ForeignKey(Razos_Social, on_delete=models.CASCADE, null=True, blank=True)
    clase = models.CharField(max_length=2, choices=Clase)
    tipo = models.CharField(max_length=2, choices=Tipo)
    contacto = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    fecha_contrato = models.DateTimeField()
    fecha_instalacion = models.DateTimeField()
    fecha_inicio = models.DateTimeField()
    observacion = models.CharField(max_length=100)
    eliminar = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    responsable = models.CharField(max_length=50)
    modelo = models.CharField(max_length=80, choices=Modelo_ProcesoIGG)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    def Contratos(self):
        return  "{}".format(self.id)

    def __str__(self):
        return self.Contratos()

class Asignacione(models.Model):
    numero = models.CharField(max_length=10)
    id_status = models.IntegerField(default=100, choices=Status_Asignacion)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField()
    fecha_asignacion = models.DateTimeField()
    contacto = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100)
    eliminar = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    fecha_codigos = models.DateTimeField(default=0)
    #fecha_despachos = models.DateTimeField(default=0)
    fecha_instalacion = models.DateTimeField()
    #transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, null=True, blank=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, null=True, blank=True)
    notificacion = models.IntegerField(default=0)
    fecha_notificacion = models.DateTimeField()
    ums_responsable = models.CharField(max_length=50)
    internet = models.IntegerField(default=0)
    revisado = models.CharField(max_length=50)
    fecha_revisado = models.DateTimeField()
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, null=True, blank=True)
    modelo = models.CharField(max_length=100, choices=Modelo_ProcesoIGG)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

class Despacho(models.Model):
    numero = models.CharField(max_length=10)
    id_status = models.IntegerField(default=50, choices=Status_Despacho)
    id_ano = models.IntegerField(default=0)
    id_cliente = models.IntegerField(default=0)
    fecha = models.DateTimeField()
    fecha_despacho = models.DateTimeField()
    contacto = models.CharField(max_length=50)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.CharField(max_length=100)
    conductor = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    guia = models.CharField(max_length=30)
    observacion = models.CharField(max_length=100)
    eliminar = models.IntegerField(default=0)
    id_seguridad = models.IntegerField(default=0)
    fecha_seguridad = models.DateTimeField()
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

class Instalacion(models.Model):
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    salas = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True)
    maquinas = models.ForeignKey(Maquina, on_delete=models.CASCADE, null=True)
    id_inspired = models.IntegerField(default=0, null=True)
    id_posicion = models.IntegerField(default=0, null=True)
    fecha_instalacion = models.DateTimeField()
    fecha_retiro = models.DateTimeField()
    id_status = models.IntegerField(default=50, choices=Status_Instalacion)
    coin_in = models.FloatField(default=0)
    coin_out = models.FloatField(default=0)
    handpay = models.FloatField(default=0)
    jackpot = models.FloatField(default=0)
    bills = models.FloatField(default=0)
    plays = models.FloatField(default=0)
    neto = models.FloatField(default=0)
    hold = models.FloatField(default=0)
    payback = models.FloatField(default=0)
    eliminar = models.IntegerField(default=0)
    porcentaje = models.FloatField(default=0)
    impuesto = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    otros = models.FloatField(default=0)
    descuentos = models.FloatField(default=0)
    dias_liquida = models.IntegerField(default=30, null=True)
    fechaliquida = models.DateTimeField()
    tipoliquida = models.CharField(max_length=2)
    #liquida =
    razon = models.ForeignKey(Razos_Social, on_delete=models.CASCADE, null=True, blank=True)
    horaliquida = models.IntegerField(default=0)
    menumix = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    variable = models.FloatField(default=0)
    cobrodia = models.FloatField(default=0)
    presupuestodia = models.FloatField(default=0)
    cobrosoporte = models.FloatField(default=0)
    montosoporte = models.FloatField(default=0)
    #idmonedasoporte =
    tarifa = models.CharField(max_length=2)
    tipooperacion = models.ForeignKey(TipoOperacion, on_delete=models.CASCADE, null=True)
    nuc = models.CharField(max_length=15, null=True)
    numeroresolucion = models.CharField(max_length=15, null=True)
    repcoljuegos = models.CharField(max_length=15, null=True)
    produccionigg = models.CharField(max_length=15, null=True)
    id_modelo_igg = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True)
    ingreso = models.FloatField(default=0)
    tipocoljuegos = models.CharField(max_length=15, null=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")


class Retiro(models.Model):
    numero = models.CharField(max_length=10)
    id_status = models.IntegerField(default=50, choices=Status_Retiro)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.IntegerField(default=0)
    fecha_retiro = models.DateTimeField()
    fecha_traslado = models.DateTimeField()
    cantidad = models.IntegerField(default=0)
    conductor = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, null=True, blank=True)
    guia = models.CharField(max_length=30)
    observacion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2)
    eliminar = models.IntegerField(default=0)
    contacto = models.CharField(max_length=50)
    fecha_recibido = models.DateTimeField()
    recibido = models.CharField(max_length=50)
    notificacion = models.IntegerField(default=0)
    fecha_notificacion = models.DateTimeField()
    ums_responsable = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado")