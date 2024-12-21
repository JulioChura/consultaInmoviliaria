# propiedades/serializers.py
from rest_framework import serializers
from .models import Propiedad

class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = ['tipo', 'zona', 'descripcion']
