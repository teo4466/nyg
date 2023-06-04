from django.db import models
import datetime

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add= True)

class Departments (models.Model):
    nombre =models.CharField(max_length=50)

class Empleados(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    contraseña = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['nombre']


class Perfilempleado(models.Model):
    empleado = models.OneToOneField(Empleados, on_delete=models.CASCADE, default=None)
    cargo = models.CharField(max_length=50)

class Accesoriosempleado(models.Model):
    nombre = models.CharField(max_length=200)
    precio= models.CharField(max_length=50, default="0")

class Accesorioentregado(models.Model):
    empleadop = models.ForeignKey(Perfilempleado, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Accesoriosempleado, on_delete=models.CASCADE)
    fechaentrega = models.DateField(auto_now= True)

class Habilitacionesempleado(models.Model):
    empleadop = models.ForeignKey(Perfilempleado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    vencimiento = models.DateField(auto_now=True)

class Capacitacion(models.Model):
    tema = models.CharField(max_length=200)
    fecha = models.DateField(auto_now=True)

class Capacitacione(models.Model):
    empleadop= models.ForeignKey(Perfilempleado, on_delete=models.CASCADE)
    capacitacion= models.ForeignKey(Capacitacion, on_delete=models.CASCADE)
    realizada= models.BooleanField(default=True)
 
class Jornadas(models.Model):
    empleadop= models.ForeignKey(Perfilempleado, on_delete=models.CASCADE)
    consentimiento = models.BooleanField(default=True)
    entrada =models.DateTimeField(auto_now_add=True)
    salida = models.DateTimeField(auto_now=False)
    horasextras = models.CharField(max_length=1)
    viaticos = models.CharField(max_length=1)
    kmsalida = models.CharField(max_length=20)
    kmllegada = models.CharField(max_length=20)
    observaciones = models.TextField(max_length=400)

class Auditoria(models.Model):
    empleadop= models.ForeignKey(Perfilempleado, on_delete=models.CASCADE)
    jornada= models.ForeignKey(Jornadas, on_delete=models.CASCADE)
    observaciones= models.TextField(max_length=300)
    calificacion= models.CharField(max_length=200)

class Visitas(models.Model) :
    jornada = models.ForeignKey(Jornadas, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    momentorecibida = models.DateField(auto_now_add=False)
    momentocumplida = models.DateField(auto_now=False)
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)

class Productos(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    codigo = models.CharField(default=0, max_length=6)
 
class DetVisitas(models.Model):
    visita = models.ForeignKey(Visitas, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0)
    observaciones= models.TextField(max_length=300)
    imagen =models.ImageField(upload_to='visitas/', null=True)

class Camiones(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=12)
    año = models.CharField(max_length=10)


class Accesorioscamion(models.Model):
    nombre = models.CharField
    fechacompra = models.DateField(auto_now=True)
    precio = models.FloatField(max_length=20)

class Checkcamion(models.Model):
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE)
    jornada = models.ForeignKey(Jornadas, on_delete=models.CASCADE)
    luces = models.BooleanField(default=True)
    limpiaparabrizas =models.BooleanField(default=True)
    frenos = models.BooleanField(default=True)
    nivelfluidos = models.BooleanField(default=True)
    cubiertas = models.BooleanField(default=True)
    plataforma = models.BooleanField(default=True)
    estructura = models.BooleanField(default=True)
    amarres = models.BooleanField(default=True)
    accesorios =models.BooleanField(default=True)
    observaciones = models.TextField(max_length=300)
    imagen =models.ImageField(upload_to='camion/')
    


class Mantenimientocamion(models.Model):
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    comentarios = models.TextField(max_length=300)
    imagen =models.ImageField(upload_to='camion/')

class Servicecamion(models.Model):
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE)
    fecharealizacion=models.DateField(auto_now_add=True)
    km = models.CharField(max_length=10)
    kmproximo= models.CharField(max_length=10)
    detalle = models.TextField(max_length=500)

class Cubiertas(models.Model):
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    kmcolocacion = models.CharField(max_length=10)
    kmrotacion =models.CharField(max_length=10)
    kmrecambio = models.CharField(max_length=10)
    fechacolocacion = models.DateField(auto_now_add=True)
    posicion = models.CharField(max_length=2)

class Habilitacionescamion(models.Model):
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fechavencimiento= models.DateTimeField(auto_now=False)
    




    


