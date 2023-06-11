from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context, loader
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

def inicio(request):
    #archivo = open (r'C:\Users\cande\OneDrive\Escritorio\Octa\Mi_primer_Django\templates\inicio.html')
    #template = Template(archivo.read())
    #archivo.close()
    
    template = loader.get_template('inicio.html')
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 == 0,
        'listado_de_numeros':list(range(25))
    }
    #contexto = Context(diccionario)
    #renderizar_template = template.render(contexto)
    renderizar_template = template.render(diccionario)
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
    