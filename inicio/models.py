from django.db import models

# Create your models here.
class Perro(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()