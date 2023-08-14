from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    etapa = models.IntegerField()
    km = models.IntegerField()
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}, {self.etapa}, {self.km}, {self.tipo}"
    
class Ciclista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    def __str__(self):
        return f"{self.nombre},{self.apellido}, {self.edad}"  

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}"  
    
class Ranking(models.Model):
    nombre = models.CharField(max_length=50)
    clasificacion = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.clasificacion}" 

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"
    
    
    