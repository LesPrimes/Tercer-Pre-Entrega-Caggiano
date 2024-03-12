from django.db import models

# Create your models here.

class Escritor(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField()

class Lector(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField()

class Articulo(models.Model):
    titulo = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    fecha_de_publicacion = models.DateTimeField()

