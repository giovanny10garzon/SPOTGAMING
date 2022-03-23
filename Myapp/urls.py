from django.urls import path

from ProcesosIGG.views import FormularioAsignarView
from . import views



urlpatterns = [
    path('', views.index_page, name='index'),
    path('sistemagestionsg/', views.pagina_inicial, name='sistemagestionsg'),
    path('asignar/', views.asignar, name='asignar'),
    path('asignacioncreada/', FormularioAsignarView.procesar_formulario, name='asignacioncreada'),
    path('conectar/', views.conectar, name='conectar'),
    path('despachar/', views.despachar, name='despachar'),
    path('instalar/', views.instalar, name='instalar'),
    path('procesoasignacion/', views.menuinstalacion, name='procesoasignacion')
]