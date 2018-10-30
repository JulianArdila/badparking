from rest_framework import serializers
from badparking.models import *
from django.contrib.auth.models import User
class TipoUsuarioSeializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = ('nombre','id')

class UsuariosSeializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True,source="user.username")
    password = serializers.CharField(write_only=True,source="user.password")
    nombre = serializers.CharField(required=False)
    apellido = serializers.CharField(required=False)
    correo = serializers.CharField(required=False)
    telefono = serializers.IntegerField(required=False)
    fecha_nacimiento = serializers.DateField(required=False)
    perfil = serializers.CharField(required=False)
    tipo = serializers.PrimaryKeyRelatedField(queryset=TipoUsuario.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'nombre', 'apellido','correo', 'fecha_nacimiento', 'perfil')
    
    def create(self, validated_data, instance=None):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])

        user.save()
        Usuarios.objects.update_or_create(user=user,**validated_data)
        usuario = Usuarios.objects.get(user=user)
        return usuario


class IngreMalParqueadoSeializer(serializers.ModelSerializer):
    class Meta:
        model = IngreMalParqueado
        fields = ('foto_ubicacion','ubicacion','fecha_de_registro','hora_de_registro','usuario','placa','confiden','id')

class CalificacionSeializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ('valor','usuario','ingreso_mal_parqueado','id')