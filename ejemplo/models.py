from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"


class Propiedades(models.Model):
    direccion = models.CharField(max_length=200)
    municipio = models.CharField(max_length=30)
    valor = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.direccion}, {self.municipio}, {self.valor}"


class Libros(models.Model):
    nombre = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
        
    def __str__(self):
        return f"{self.nombre}, {self.autor}, {self.genero}"



