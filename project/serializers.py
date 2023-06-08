from rest_framework import serializers
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
        model= Empleados
        fields= ("id", "nombre", "direccion", "telefono", "email", "contraseña")

class PerfilempleadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Perfilempleado
        fields= "__all__"

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'cargo': instance.cargo,
            'empleado': instance.empleado.nombre
        }


class AccesoriosempleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Accesoriosempleado
        fields = "__all__"

class AccesorioentregadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Accesorioentregado
        fields=("id", "empleadop", "nombre", "fechaentrega")

class HabilitacionesempleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Habilitacionesempleado
        fields=("id", "empleadop","nombre", "vencimiento")

class CapacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Capacitacion
        fields=("id", "tema", "fecha")

class CapacitacioneSerializer(serializers.ModelSerializer):
    class Meta:
        model= Capacitacione
        fields=("id", "empleadop", "capacitacion", "realizada")

class JornadasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Jornadas
        fields= "__all__"

class VisitasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Visitas
        fields=("id", "jornada", "cliente", "momentorecibida", "momentocumplida", "direccion", "estado")

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
         model= Auditoria
         fields= ("id","empleadop", "jornada", "observaciones", "calificacion")

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productos
        fields=("id", "nombre", "codigo")

class DetvisitasSerializer(serializers.ModelSerializer):
    class Meta:
        model= DetVisitas
        fields=("id", "visita", "producto", "cantidad", "observaciones","imagen")

class CamionesSerializer(serializers.ModelSerializer):
    class Meta:
            model= Camiones
            fields=("id", "marca", "modelo", "capacidad", "año")

class AccesorioscamionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Accesorioscamion
        fields=("id", "nombre", "fechacompra", "precio")

class CheckcamionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Checkcamion
        fields= ("id", "camion", "jornada", "luces", "limpiaparabrizas", "frenos", "nivelfluidos","cubiertas", "plataforma", "estructura", "amarres", "accesorios", "observaciones", "imagen")

class ManteniemientocamionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Mantenimientocamion
        fields= '__all__'

class ServicecamionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Servicecamion
        fields= '__all__'

class CubiertasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cubiertas
        fields= '__all__'
        
class HabilitacionescSerializer(serializers.ModelSerializer):
    class Meta:
        model= Habilitacionescamion
        fields= ("camion", "nombre", "fechavencimiento")
        

