from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context
#v1
# def inicio(request):
#     return HttpResponse('Hola soy Octavio')
def inicio(request):
    archivo = open (r'C:\Users\cande\OneDrive\Escritorio\Octa\Mi_primer_Django\templates\inicio.html')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    renderizar_template = template.render(contexto)
    return HttpResponse(renderizar_template)

def segunda_vista(request):
    return HttpResponse('<h1>soy la segunda vista<h2>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'fecha actual: {fecha}')
def saludar(request):
    return HttpResponse('Bienvenidos!!')
def bienvenida(request,nombre,apellido):
    return HttpResponse(f'Bienvenido/a {nombre.title()} {apellido.title()}')
    