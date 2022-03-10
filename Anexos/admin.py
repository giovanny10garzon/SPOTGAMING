from django.contrib import admin
from .models import *
# Register your models here.
class RazonSocialAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'id_inspired', 'nombre', 'activo')

class DepartamentoAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'dane', 'activo')

class CiudadAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'dane', 'activo', 'departamentos')

class FamiliaAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'activo')

class TipoJuegoAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'activo')

class JuegoAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'id_inspired', 'nombre', 'tipo_juego', 'activo')

class MarcaAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'activo')

class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'activo')

class TecnicoAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'activo')

class CondicionAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'activo')

class StatusAdmin (admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'activo')

class CategoriaFallaadmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'activo')

class PiezaAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id_codigo', 'nombre', 'activo')

class GrupoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('id', 'id_codigo', 'nombre', 'activo')

admin.site.register(Razos_Social, RazonSocialAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(FamiliaMaquina, FamiliaAdmin)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(TipoJuego, TipoJuegoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Tecnico, TecnicoAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Condicion, CondicionAdmin)
admin.site.register(CategoriaFalla, CondicionAdmin)
admin.site.register(Pieza, PiezaAdmin)
admin.site.register(Grupos, GrupoAdmin)

