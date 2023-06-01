from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add= True)

class Departments(models.Model):
    nombre =models.CharField(max_length=50)

