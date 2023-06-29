from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=40)
    valor=models.CharField(max_length=40)
