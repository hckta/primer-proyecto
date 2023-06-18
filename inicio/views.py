from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context, loader
from inicio.models import Perro
from django.shortcuts import render
#v1
# def inicio(request):
#     return HttpResponse('Hola soy Octavio')
#v2
# def inicio(request):
#     archivo = open (r'C:\Users\cande\OneDrive\Escritorio\Octa\Mi_primer_Django\templates\inicio.html')
#     template = Template(archivo.read())
#     archivo.close()
#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos': segundos,
#         'segundo_par': segundos%2 == 0,
#         'segundo_redondo': segundos%10 == 0,
#         'listado_de_numeros':list(range(25))
#     }
#     contexto = Context(diccionario)
#     renderizar_template = template.render(contexto)
#     return HttpResponse(renderizar_template)
#v3

# def inicio(request):
#     #archivo = open (r'C:\Users\cande\OneDrive\Escritorio\Octa\Mi_primer_Django\templates\inicio.html')
#     #template = Template(archivo.read())
#     #archivo.close()
    
#     template = loader.get_template('inicio.html')
#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos': segundos,
#         'segundo_par': segundos%2 == 0,
#         'segundo_redondo': segundos%10 == 0,
#         'listado_de_numeros':list(range(25))
#     }
#     #contexto = Context(diccionario)
#     #renderizar_template = template.render(contexto)
#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)
#4
def prueba(request):
    
    # template = loader.get_template('inicio.html')
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 == 0,
        'listado_de_numeros':list(range(25))
    }
    # renderizar_template = template.render(diccionario)
    # return HttpResponse(renderizar_template)
    return render(request,'inicio/prueba.html', diccionario )
def inicio(request):
    return render(request, 'inicio/inicio.html')
def segunda_vista(request):
    return HttpResponse('<h1>soy la segunda vista<h2>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'fecha actual: {fecha}')
def saludar(request):
    return HttpResponse('Bienvenidos!!')
def bienvenida(request,nombre,apellido):
    return HttpResponse(f'Bienvenido/a {nombre.title()} {apellido.title()}')
#v1
# def crear_perro(request, nombre, edad):
#     template = loader.get_template('crear_perro.html')
#     perro = Perro(nombre=nombre, edad=edad)
#     perro.save()
#     diccionario = {
#         'perro': perro,
#     }
#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)
#v2

def crear_perro(request, nombre, edad):
    perro = Perro(nombre=nombre, edad=edad)
    perro.save()
    diccionario = {
        'perro': perro,
    }
    return render(request,'inicio/crear_perro.html', diccionario)