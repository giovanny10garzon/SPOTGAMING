from django.shortcuts import render
from django.conf import settings

import Maestro
from Auditoria.models import Liquidacione
from Maestro.models import *
from Anexos.models import *

# Create your views here.
from ProcesosIGG.models import Asignacione

def spotgaming(request):

    return render(request, "spotgaming.html")

def menuinstalacion(request):

    return render(request, "menuinstalacion.html")

def menuauditoria(request):

    return render(request, "menuauditoria.html")

def menumaestro(request):

    return render(request, "menumaestro.html")

def asignar(request):
    asignaciones = Asignacione.objects.all()
    listaclientes = Cliente.objects.all()

    return render(request, "asignar.html", {
        'nombre': 'Asignacion',
        'asignaciones' : asignaciones,
        'clientes': listaclientes
    })

def conectar(request):
    clientesconectar = Maquina.objects.all()

    return render(request, "conectar.html", {
        'conectar' : 'conexion',
        'conexiones' : clientesconectar
    })

def despachar(request):

    return render(request, "despachar.html")

def instalar(request):

    return render(request, "instalar.html")

def retirar(request):
    listaclientes = Cliente.objects.all()
    formasenvios = Transporte.objects.all()

    return render(request, "retirar.html", {
        'conectado': 'conexion',
        'clientes': listaclientes,
        'transportes' : formasenvios
    })

def liquidar(request):
    liquidaciones = Liquidacione.objects.all()

    return render(request, "liquidar.html", {
        'liquidar' : 'Liquidacion',
        'liquidaciones' : liquidaciones
    })

def listaasignar(request):
    listasasignar = Asignacione.objects.all()
    listaclientes = Cliente.objects.all()

    return render(request, "listaasignacion.html", {
        'asignado' : 'asignacion',
        'asignaciones' : listasasignar,
        'clientes' : listaclientes
    })

def listaconectar(request):
    listaconectar = Asignacione.objects.all()
    listaclientes = Cliente.objects.all()

    return render(request, "listaconectar.html", {
        'conectado' : 'conexion',
        'asignaciones' : listaconectar,
        'clientes': listaclientes
    })

def listadespachar(request):
    listaconectar = Asignacione.objects.all()
    listaclientes = Cliente.objects.all()

    return render(request, "listadespachar.html", {
        'conectado' : 'conexion',
        'asignaciones' : listaconectar,
        'clientes': listaclientes
    })

def listainstalar(request):
    listaconectar = Asignacione.objects.all()
    listaclientes = Cliente.objects.all()

    return render(request, "listainstalar.html", {
        'conectado' : 'conexion',
        'asignaciones' : listaconectar,
        'clientes': listaclientes
    })

def listaretiros(request):
    listaclientes = Cliente.objects.all()

    return render(request, "listaretiros.html", {
        'conectado': 'conexion',
        'clientes': listaclientes
    })

def listacliente(request):
    listaclientes = Cliente.objects.all()

    return render(request, "listacliente.html", {
        'conectado': 'conexion',
        'clientes': listaclientes
    })

def listasala(request):
    listaclientes = Sala.objects.all()

    return render(request, "listasala.html", {
        'conectado': 'conexion',
        'clientes': listaclientes
    })

def listamaquina(request):
    listaclientes = Maquina.objects.all()

    return render(request, "listamaquina.html", {
        'conectado': 'conexion',
        'clientes': listaclientes
    })