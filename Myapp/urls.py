from django.urls import path

from django.contrib import admin
from . import views


urlpatterns = [
    #path('', admin.site.urls, name='SpotGamingAdmin'),
    path('spotgaming/', views.spotgaming, name='spotgaming'),
    path('sistemagestionsg/', views.menuinstalacion, name='sistemagestionsg'),
    path('asignar/', views.asignar, name='asignar'),
    path('retirar/', views.retirar, name='retirar'),
    path('asignacioncreada/', views.asignar, name='asignacioncreada'),
    path('conectar/', views.conectar, name='conectar'),
    path('despachar/', views.despachar, name='despachar'),
    path('instalar/', views.instalar, name='instalar'),
    path('procesoasignacion/', views.menuinstalacion, name='procesoasignacion'),
    path('liquidar/', views.liquidar, name='liquidar'),
    path('listaasignacion/', views.listaasignar, name='listaasignacion'),
    path('listaconectar/', views.listaconectar, name='listaconectar'),
    path('listadespachar/', views.listadespachar, name='listadespachar'),
    path('listainstalar/', views.listainstalar, name='listainstalar'),
    path('listaretiros/', views.listaretiros, name='listaretiros'),
    path('menuauditoria/', views.menuauditoria, name='menuauditoria'),
    path('menumaestro/', views.menumaestro, name='menumaestro'),
    path('listacliente/', views.listacliente, name='listacliente'),
    path('listasala/', views.listasala, name='listasala'),
    path('listamaquina/', views.listamaquina, name='listamaquina')
]

