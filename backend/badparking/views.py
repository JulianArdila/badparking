from django.shortcuts import render
from django.shortcuts import render_to_response
from rest_framework import generics
from badparking.models import *
from badparking.serializer import *
from badparking.permissions import IsPostOrIsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


def principal(request):
    tipo = TipoUsuario.objects.all()
    return render(request,"paginaPrincipal.html", {'tipo': tipo})

@permission_classes((AllowAny,))
class TipoUsuarioList(generics.ListAPIView):
    serializer_class = TipoUsuarioSeializer
    queryset = TipoUsuario.objects.all()

class TipoUsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TipoUsuarioSeializer
    queryset = TipoUsuario.objects.all()

@permission_classes((IsPostOrIsAuthenticated, ))    
class UsuariosList(generics.ListCreateAPIView):
    serializer_class = UsuariosSeializer
    queryset = Usuarios.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user_id',)


class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuariosSeializer
    queryset = Usuarios.objects.all()


class IngreMalParqueadoList(generics.ListCreateAPIView):
    serializer_class = IngreMalParqueadoSeializer
    queryset = IngreMalParqueado.objects.all()


class IngreMalParqueadoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IngreMalParqueadoSeializer
    queryset = IngreMalParqueado.objects.all()


class CalificacionList(generics.ListCreateAPIView):
    serializer_class = CalificacionSeializer
    queryset = Calificacion.objects.all()


class CalificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CalificacionSeializer
    queryset = Calificacion.objects.all()
