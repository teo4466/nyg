from rest_framework import serializers
from .models import Clientes

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields =("id", "nombre", "direccion", "telefono")
        read_only_fields = ("created_at",)