from django.shortcuts import render
from django.conf import settings
from Maestro.models import *

# Create your views here.
def index_page(request):

    return render(request, 'myapp/index.html', {
        'title': 'soy index'
    })

def pagina_inicial(request):
    clientes = Cliente.objects.all()
    return render(request, 'myapp/sistemagestionsg.html', {
        'title': 'SISTEMA GESTION SG',
        'clientes': clientes
    })
def menuinstalacion(request):

    return render(request, "menuinstalacion.html")

def asignar(request):

    return render(request, "asignar.html")

def conectar(request):

    return render(request, "conectar.html")

def despachar(request):

    return render(request, "despachar.html")

def instalar(request):

    return render(request, "instalar.html")