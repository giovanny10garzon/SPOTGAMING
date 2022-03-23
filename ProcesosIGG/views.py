from django.shortcuts import render
from django.http import HttpRequest
from ProcesosIGG.formasignar import FormularioAsignar
# Create your views here.



class FormularioAsignarView(HttpRequest):

    def index(request):
        asignar = FormularioAsignar()
        return render(request, "asignar.html", {"form":asignar})

    def procesar_formulario(request):
        asignar = FormularioAsignar()
        if asignar.is_valid():
            asignar.save()
            asignar = FormularioAsignar()

        return  render(request, "asignarindex.html", {"form":asignar, "mensaje": 'ok'})

