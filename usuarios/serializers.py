from rest_framework import serializers
from .models import Estudiante, Docente

# class UsuarioSerializer(serializers.ModelSerializer):
#     user=serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = Usuario
#         fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Estudiante
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Docente
        fields = '__all__'
