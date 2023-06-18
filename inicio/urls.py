from django.urls import path
from inicio import views

urlpatterns = [
    
    path('', views.inicio),
    path('prueba/',views.prueba),
    path('segunda-vista/',views.segunda_vista),
    path('fecha-actual/', views.fecha_actual),
    path('saludar/', views.saludar),
    path('bienvenida/<str:nombre>/<str:apellido>/', views.bienvenida),
    path('crear-perro/<str:nombre>/<int:edad>/', views.crear_perro),
]
