from django.shortcuts import render
from appcoder.models import Curso
from django.http import HttpResponse




# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):

    return HttpResponse("Estas en cursos")

def estudiantes(request):
    
    
    return HttpResponse("Estas en estudiantes")

def profesores(request):


    return HttpResponse("Estas en el profesores")

def entregables(request):


    return HttpResponse("Estas en entregables")



# def listado_cursos(request):
#     cursos = Curso.objects.all()

#     cadena_respuesta = ""
#     for curso in cursos:
#         cadena_respuesta += curso.nombre + " | "

#         return HttpResponse(cadena_respuesta)
