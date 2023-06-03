from rest_framework import serializers
from .models import Clientes
from .models import *

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields =("id", "nombre", "direccion", "telefono")
        read_only_fields = ("created_at",)

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Departments
        fields=("id", "nombre",)
        read_only_fields = ("created_at",)

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        models= Empleados
        field= ("id", "nombre", "direccion", "telefono", "email", "contraseña")

class PerfilempleadoSerializer(serializers.ModelSerializer):
    class Meta:
        models=Perfilempleado
        field=("id" ,"empleado", "cargo")

class AccesoriosempleadoSerializer(serializers.ModelSerializer):
    class Meta:
        models= Accesoriosempleado
        field =("id", " nombre")

class AccesorioentregadoSerializer(serializers.ModelSerializer):
    class Meta:
        models= Accesorioentregado
        field=("id", "empleadop", "nombre", "fechaentrega")

class HabilitacionesempleadoSerializer(serializers.ModelSerializer):
    class Meta:
        models= Habilitacionesempleado
        field=("id", "empleadop","nombre", "vencimiento")

class CapacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        models= Capacitacion
        field=("id", "empleadop", "tema", "fecha")

class JornadasSerializer(serializers.ModelSerializer):
    class Meta:
        models= Jornadas
        field= ("id", "empleado", "concentimiento", "entrada", "salida", "horasextras", "viaticos", "kmsalida", "kmllegada", "observaciones")

class VisitasSerializer(serializers.ModelSerializer):
    class Meta:
        models= Visitas
        field=("id", "jornada", "cliente", "momentorecibida", "momentocumplida", "direccion", "cumplida")

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        models= Productos
        field=("id", "nombre", "codigo")

class DetvisitasSerializer(serializers.ModelSerializer):
    class Meta:
        models= DetVisitas
        field=("id", "visita", "producto", "cantidad", "observaciones","imagen")

class CamionesSerializer(serializers.ModelSerializer):
    class Meta:
            models= Camiones
            field=("id", "marca", "modelo", "capacidad", "año")

class AccesorioscamionSerializer(serializers.ModelSerializer):
    class Meta:
        models= Accesorioscamion
        field=("id", "nombre", "fechacompra", "precio")

class CheckcamionSerializer(serializers.ModelSerializer):
    class Meta:
        models=Accesorioscamion
        field= ("id", "camion", "jornada", "luces", "limpiaparabrizas", "frenos", "nivelfluidos","cubiertas", "plataforma", "extructuras", "amarres", "accesorios", "observaciones", "imagen")

class ManteniemientocamionSerializer(serializers.ModelSerializer):
    class Meta:
        models= Mantenimientocamion
        field= ("id", "camion", "fecha", "comentarios", "imagen")

class ServicecamionSerializer(serializers.ModelSerializer):
    class Meta:
        models= Servicecamion
        field=("id", "camion", "fecharealizacion", "km", "kmproximo", "detalle")

class CubiertasSerializer(serializers.ModelSerializer):
    class Meta:
        models= Cubiertas
        field= ("id", "camion", "marca", "kmcolocacion", "kmrotacion", "kmrecambio", "fechacolocacion", "posicion")
        


        

