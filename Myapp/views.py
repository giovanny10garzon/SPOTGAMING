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