# from django.http import HttpResponse
# from datetime import datetime
# from django.template import Template, Context, loader



# def greeting(request): # Las vistas siempre van a recibir el request
#     return HttpResponse(""" 
#     <h1>Hola coders! </h1>
#     <p style="color:red">Esto es una prueba</p>
#     """)  

# def iniciar_sesion(request):
#    return HttpResponse("Pasame tu user name y tu numero por whatsapp")


# def dia_hoy(request, nombre):
#     hoy = datetime.now()
#     respuesta = f"hoy es {hoy}- Bienvenid@{nombre}"
#     return HttpResponse(respuesta)


# def edad(request,anios):
#     years = int(anios)
#     valor = datetime.now().year - years
#     return HttpResponse(f"naciste en {valor}")

# def vista_pantilla(request):
#     # Abrimos el archivo
#     archivo = open(r"C:\Users\israe\Desktop\proyectoDjango\codigo\proyectocoder\templates\plantilla_bonita.html")

#     #Creamos el objeto plantilla
#     plantilla = Template(archivo.read())

#     # Cerramos el archivo para liberar recursos
#     archivo.close()

#     # Diccionario con datos para la plantilla

#     datos = {"nombre":"israel", "fecha":datetime.now(), "apellido":"balbuena", "Edad":29}

#     # Creamos el contexto
#     contexto = Context(datos)    

#     # Renderizamos el archivo para generar la respuesta
#     documento = plantilla.render(contexto)

#     #Retornamos la respuest
#     return HttpResponse(documento)


# def vista_listado_alumnos(request):

#     # abrimos el archivo
#     archivo = open(r"C:\Users\israe\Desktop\proyectoDjango\codigo\proyectocoder\templates\listado_alumnos.html")

#     #Creamos el archivo Template

#     plantilla = Template(archivo.read())

#     #cerramos el archivo para liberar recursos
#     archivo.close()

#     # creamos el diccionario de datos

#     listado_alumnos = ["Leonel Gareis","Agustin Ruso","Cristian Garcia","Angelo Pettinari","Diego Ibarra", "Santiago Ortiz","Barbara Vivante","Barbara Nose"]
#     datos = {"tecnologia":"Python", "listado_alumnos": listado_alumnos}

#     #Creamos el contexto

#     contexto = Context(datos)

#     documento = plantilla.render(contexto)

#     return HttpResponse(documento)

# def vista_listado_alumnos2(request):

#     listado_alumnos = ["Leonel Gareis","Agustin Ruso","Cristian Garcia","Angelo Pettinari","Diego Ibarra", "Santiago Ortiz","Barbara Vivante","Barbara Nose"]
#     datos = {"tecnologia":"Python", "listado_alumnos": listado_alumnos}

#     plantilla =loader.get_template("listado_alumnos.html")
#     documento = plantilla.render(datos)

#     return HttpResponse(documento)


# def vista_plantilla2(request):

#     datos = {"nombre":"israel", "fecha":datetime.now(), "apellido":"balbuena", "Edad":29}
    
#     plantilla = loader.get_template("plantilla_bonita.html")

#     documento = plantilla.render(datos)

#     return HttpResponse(documento)
 
