from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientesSerializer

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset= Departments.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= DepartmentsSerializer

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset= Empleados.objects.all()
    serializer_class= EmpleadosSerializer

class PerfilempleadoViewSet(viewsets.ModelViewSet):
    queryset=Perfilempleado.objects.all()
    serializer_class= PerfilempleadoSerializer

class AccesoriosempleadoViewSet(viewsets.ModelViewSet):
    queryset= Accesoriosempleado.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= AccesorioscamionSerializer

class AccesorioentregadoViewset(viewsets.ModelViewSet):
    queryset=Accesorioentregado.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=AccesorioentregadoSerializer

class HabilitacionesempleadoViewSet(viewsets.ModelViewSet):
    queryset= Habilitacionesempleado.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=HabilitacionesempleadoSerializer

class CapacitacionViewSet(viewsets.ModelViewSet):
    queryset= Capacitacion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=CapacitacionSerializer

class CapacitacioneViewSet(viewsets.ModelViewSet):
    queryset= Capacitacione.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= CapacitacioneSerializer

class CombustibleViewSet(viewsets.ModelViewSet):
    queryset= Combustible.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=CombustibleSerializer

class GastosViewSet(viewsets.ModelViewSet):
    queryset= Gastos.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=GastoSerializer


class JornadasViewSet(viewsets.ModelViewSet):
    queryset= Jornadas.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= JornadasSerializer

class VisitasViewSet(viewsets.ModelViewSet):
    queryset= Visitas.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= VisitasSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset= Productos.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= ProductosSerializer

class DetvisitasViewSet(viewsets.ModelViewSet):
    queryset= DetVisitas.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= DetvisitasSerializer

class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset= Auditoria.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= AuditoriaSerializer

class CamionesViewSet(viewsets.ModelViewSet):
    queryset= Camiones.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= CamionesSerializer

class AccessoriocamionViewSet(viewsets.ModelViewSet):
    queryset= Accesorioscamion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= AccesorioscamionSerializer

class CheckcamionViewSet(viewsets.ModelViewSet):
    queryset= Checkcamion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= CheckcamionSerializer

class MantenimientocamionViewSet(viewsets.ModelViewSet):
    queryset= Mantenimientocamion.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= ManteniemientocamionSerializer

class ServicecamionViewset(viewsets.ModelViewSet):
    queryset= Servicecamion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= ServicecamionSerializer

class CubiertaViewSet(viewsets.ModelViewSet):
      queryset= Cubierta.objects.all()
      permission_classes=[permissions.AllowAny]
      serializer_class= CubiertaSerializer

class HabilitacionescViewSet(viewsets.ModelViewSet):
    queryset= Habilitacionescamion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= HabilitacionescSerializer

class EnvasesViewSet(viewsets.ModelViewSet):
    queryset= Envases.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= EnvasesSerializer
