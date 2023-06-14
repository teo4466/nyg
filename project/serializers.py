from rest_framework import serializers
from .models import *

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields= "__all__"
        read_only_fields = ("created_at",)

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Departments
        fields=("id", "nombre",)
        read_only_fields = ("created_at",)

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Empleados
        fields= "__all__"

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
        fields= "__all__"

class HabilitacionesempleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Habilitacionesempleado
        fields= "__all__"

class CapacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Capacitacion
        fields= "__all__"

class CapacitacioneSerializer(serializers.ModelSerializer):
    class Meta:
        model= Capacitacione
        fields= "__all__"

class JornadasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Jornadas
        fields= "__all__"

      
class VisitasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Visitas
        fields="__all__"

  
class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
         model= Auditoria
         fields= "__all__"

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productos
        fields= "__all__"

class DetvisitasSerializer(serializers.ModelSerializer):
    class Meta:
        model= DetVisitas
        fields= "__all__"

class CamionesSerializer(serializers.ModelSerializer):
    class Meta:
            model= Camiones
            fields= "__all__"

class CombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Combustible
        fields="__all__"

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gastos
        fields="__all__"

class AccesorioscamionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Accesorioscamion
        fields= "__all__"

class CheckcamionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Checkcamion
        fields= "__all__"
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
        fields= "__all__"
        

