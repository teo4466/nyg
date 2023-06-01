from .models import Clientes
from rest_framework import viewsets, permissions
from .serializers import ClientesSerializer
from .serializers import DepartmentsSerializer
from .models import Departments

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientesSerializer

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset= Departments.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= DepartmentsSerializer