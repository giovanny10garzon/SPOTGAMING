from django.contrib import admin
from .models import *
# Register your models here.

class LiquidacionAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('numero', 'clientes', 'razon', 'id_status', 'nro_maquinas', 'neto', 'desbalance', 'suma_impuestos', 'monto', 'monto_igg')

admin.site.register(Liquidacione, LiquidacionAdmin)