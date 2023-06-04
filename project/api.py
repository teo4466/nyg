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
    permission_classes=[permissions.AllowAny]
    serializer_class= EmpleadosSerializer

class PerfilempleadoViewSet(viewsets.ModelViewSet):
    queryset=Perfilempleado.objects.all()
    permission_classes= [permissions.AllowAny]
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
    serializers_class= CheckcamionSerializer

class MantenimientocamionViewSet(viewsets.ModelViewSet):
    queryset= Mantenimientocamion.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= ManteniemientocamionSerializer

class ServicecamionViewset(viewsets.ModelViewSet):
    queryset= Servicecamion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= ServicecamionSerializer

class CubiertasViewSet(viewsets.ModelViewSet):
    queryset= Cubiertas
    permission_classes=[permissions.AllowAny]
    serializer_class= CubiertasSerializer

class HabilitacionescViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= Habilitacionescamion
    permission_classes=[permissions.AllowAny]
    serializer_class= HabilitacionescSerializer
