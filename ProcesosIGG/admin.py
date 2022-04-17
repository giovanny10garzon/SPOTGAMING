from django.contrib import admin
from .models import *
# Register your models here.
class ContratoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id', 'clientes', 'razon', 'clase', 'tipo', 'modelo', 'id_status', 'fecha_contrato', 'fecha_instalacion')

class AsignacionAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id', 'numero', 'clientes', 'contacto','stado', 'fecha_asignacion', 'modelo')
    autocomplete_fields = ['clientes']


class DespachoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id', 'numero', 'id_cliente', 'id_status', 'fecha_despacho')

class RetiroAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id', 'numero', 'clientes', 'id_status')

class InstalacionAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id', 'clientes', 'id_status')

admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Asignacione, AsignacionAdmin)
admin.site.register(Despacho, DespachoAdmin)
admin.site.register(Retiro, RetiroAdmin)
admin.site.register(Instalacion, InstalacionAdmin)