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

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']


class Perfilempleado(models.Model):
    empleado = models.OneToOneField(Empleados, on_delete=models.CASCADE, default=None)
    cargo = models.CharField(max_length=50)

   
class Accesoriosempleado(models.Model):
    nombre = models.CharField(max_length=200)
    precio= models.CharField(max_length=50, default="0")

class Accesorioentregado(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, default=None)
    nombre = models.ForeignKey(Accesoriosempleado, on_delete=models.CASCADE, default=None)
    fechaentrega = models.DateField(auto_now= True)

class Habilitacionesempleado(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=200)
    vencimiento = models.DateField(auto_now=True)

class Capacitacion(models.Model):
    tema = models.CharField(max_length=200)
    fecha = models.DateField(auto_now=True)

class Capacitacione(models.Model):
    empleado= models.ForeignKey(Empleados, on_delete=models.CASCADE , default=None)
    capacitacion= models.ForeignKey(Capacitacion, on_delete=models.CASCADE)
    realizada= models.BooleanField(default=True)

class Camiones(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=12)
    año = models.CharField(max_length=10)
 
class Jornadas(models.Model):
    empleado= models.ForeignKey(Empleados, on_delete=models.CASCADE, default=None)
    camion=models.ForeignKey(Camiones, on_delete=models.CASCADE, default=None)
    consentimiento = models.BooleanField(default=True)
    entrada =models.DateTimeField(auto_now_add=True)
    salida = models.DateTimeField(auto_now=False)
    horasextras = models.CharField(max_length=1)
    viaticos = models.CharField(max_length=1)
    kmsalida = models.CharField(max_length=20)
    kmllegada = models.CharField(max_length=20)
    observaciones = models.TextField(max_length=400)

class Auditoria(models.Model):
    empleado= models.ForeignKey(Empleados, on_delete=models.CASCADE, default=None)
    jornada= models.ForeignKey(Jornadas, on_delete=models.CASCADE)
    observaciones= models.TextField(max_length=300)
    calificacion= models.CharField(max_length=200)

class Visitas(models.Model) :
    jornada = models.ForeignKey(Jornadas, on_delete=models.CASCADE, default=None)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, default=None)
    momentorecibida = models.DateTimeField(auto_now_add=False)
    momentocumplida = models.DateTimeField(auto_now=False)
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    observacion= models.TextField(max_length=300, default=None)
    

class Productos(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    codigo = models.CharField(default=0, max_length=6)
 
class DetVisitas(models.Model):
    visita = models.ForeignKey(Visitas, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0)
    observaciones= models.TextField(max_length=300)
    imagen =models.ImageField(upload_to='visitas/', null=True)


class Accesorioscamion(models.Model):
    nombre = models.CharField(max_length=100, default=None)
    fechacompra = models.DateField(auto_now=True)
    precio = models.FloatField(max_length=20)

class Checkcamion(models.Model):
    empleado=models.ForeignKey(Empleados, on_delete=models.CASCADE, default=None)
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE, default=None)
    jornada = models.ForeignKey(Jornadas, on_delete=models.CASCADE, default=None)
    luces = models.CharField(max_length=10,default=True)
    limpiaparabrizas =models.CharField(max_length=10,default=True)
    frenos = models.CharField(max_length=10,default=True)
    nivelfluidos = models.CharField(max_length=10,default=True)
    cubiertas = models.CharField(max_length=10,default=True)
    plataforma = models.CharField(max_length=10,default=True)
    estructura = models.CharField(max_length=10,default=True)
    amarres = models.CharField(max_length=10,default=True)
    accesorios =models.CharField(max_length=10,default=True)
    observaciones = models.TextField(max_length=300)
    imagen =models.ImageField(upload_to='camion/', null=True)
    imagen2 =models.ImageField(upload_to='camion/', null=True)
    firma =models.ImageField(upload_to='camion/', null=True)
    
    
class Mantenimientocamion(models.Model):
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE, default=None)
    fecha = models.DateField(auto_now_add=True)
    comentarios = models.TextField(max_length=300)
    imagen1 =models.ImageField(upload_to='camion/', null=True)
    imagen2 =models.ImageField(upload_to='camion/', null=True)

class Servicecamion(models.Model):
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE, default=None)
    fecharealizacion=models.DateField(auto_now_add=True)
    km = models.CharField(max_length=10)
    kmproximo= models.CharField(max_length=10)
    detalle = models.TextField(max_length=500)
    imagen1 =models.ImageField(upload_to='camion/', null=True)


class Cubiertas(models.Model):
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE, default=None)
    marca = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50, default=True)
    kmcolocacion = models.CharField(max_length=10)
    kmrotacion =models.CharField(max_length=10)
    kmrecambio = models.CharField(max_length=10)
    fechacolocacion = models.DateField(auto_now_add=True)
    posicion = models.CharField(max_length=2)
    posicion2 = models.CharField(max_length=2)

class Combustible(models.Model):
    fechavencimiento= models.DateTimeField(auto_now=False)
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE, default=None)
    km = models.CharField(max_length=10)
    Litros = models.CharField(max_length=10)
    imagen1 =models.ImageField(upload_to='camion/', null=True)

class Gastos(models.Model):
     fechavencimiento= models.DateTimeField(auto_now=False)
     camion = models.ForeignKey(Camiones, on_delete=models.CASCADE, default=None)
     tema = models.CharField(max_length=10)
     descripcion = models.CharField(max_length=10)
     imagen1 =models.ImageField(upload_to='camion/', null=True)

    

class Habilitacionescamion(models.Model):
    camion = models.ForeignKey(Camiones, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fechavencimiento= models.DateTimeField(auto_now=False)
    




    


