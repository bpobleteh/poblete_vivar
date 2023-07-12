from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=40)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    fotografia = models.ImageField(upload_to='Septima', default='default.jpg')

