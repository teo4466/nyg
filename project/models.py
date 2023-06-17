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
    empleado= models.CharField(max_length=50)
    camion=models.CharField(max_length=10)
    consentimiento = models.BooleanField(default=True)
    entrada =models.CharField(max_length=50)
    salida = models.CharField(max_length=50, default=None)
    horasextras = models.CharField(max_length=1, default=None)
    viaticos = models.CharField(max_length=1, default=None)
    kmsalida = models.CharField(max_length=20)
    kmllegada = models.CharField(max_length=20, default=None)
    observaciones = models.TextField(max_length=400, default=True)

class Auditoria(models.Model):
    fecha=models.CharField(max_length=50, default="")
    empleado= models.CharField(max_length=50)
    observaciones= models.TextField(max_length=300)
    calificacion= models.CharField(max_length=200)

class Visitas(models.Model) :
    ciudad=models.CharField(max_length=20, default=True)
    empleado= models.CharField(max_length=50)
    cliente = models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    momentorecibida = models.CharField(max_length=50,default=True)
    momentocumplida = models.CharField(max_length=50, default=False)
    estado = models.CharField(max_length=20,default=False)
    observacion= models.TextField(max_length=300, default=False)
    imagen =models.ImageField(upload_to='visitas/', default=False)
    

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
    fechacompra = models.CharField(max_length=50, default="")
    precio = models.FloatField(max_length=20)

class Checkcamion(models.Model):
    fecha=models.CharField(max_length=50, default="")
    empleado=models.CharField(max_length=50)
    camion = models.CharField(max_length=20)
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
    camion = models.CharField(max_length=20)
    fecha = models.CharField(max_length=50, default="")
    comentarios = models.TextField(max_length=300)
    imagen1 =models.ImageField(upload_to='camion/', null=True)
    imagen2 =models.ImageField(upload_to='camion/', null=True)

class Servicecamion(models.Model):
    camion = models.CharField(max_length=20)
    fecharealizacion=models.CharField(max_length=50, default="")
    km = models.CharField(max_length=10)
    kmproximo= models.CharField(max_length=10)
    detalle = models.TextField(max_length=500)
    imagen1 =models.ImageField(upload_to='camion/', null=True)


class Cubiertas(models.Model):
    camion = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    #kmcolocacion = models.CharField(max_length=10)
    #kmrotacion =models.CharField(max_length=10, default=True)
    #kmrecambio = models.CharField(max_length=10, default=True)
    #fechac = models.CharField(max_length=50)
    #posicion = models.CharField(max_length=20)
    #posicion2 = models.CharField(max_length=20, default=True)

class Combustible(models.Model):
    fecha= models.CharField(max_length=50, default="")
    camion = models.CharField(max_length=20)
    km = models.CharField(max_length=10)
    Litros = models.CharField(max_length=10)
    importe= models.CharField(max_length=20, default=False)
    imagen1 =models.ImageField(upload_to='camion/', null=True)


class Gastos(models.Model):
     fecha= models.CharField(max_length=50, default="")
     camion = models.CharField(max_length=20)
     tema = models.CharField(max_length=10)
     descripcion = models.CharField(max_length=10)
     imagen1 =models.ImageField(upload_to='camion/', null=True)

    

class Habilitacionescamion(models.Model):
    camion = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    fechavencimiento= models.CharField(max_length=50, default="")
    




    


