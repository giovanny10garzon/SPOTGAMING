from django.contrib import admin
from .models import *

# Register your models here.
class InventarioAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id', 'descripcion', 'id_status', 'fecha_despacho', 'clientes', 'tipo')
    list_filter = ('tipo', )
    search_fields = ('serial',)

admin.site.register(Inventario, InventarioAdmin)