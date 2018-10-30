from django.shortcuts import render
from django.shortcuts import render_to_response
from rest_framework import generics
from badparking.models import *
from badparking.serializer import *
# Create your views here.

def principal(request):
    return render_to_response("paginaPrincipal.html")

class TipoUsuarioList(generics.ListAPIView):
    serializer_class = TipoUsuarioSeializer
    queryset = TipoUsuario.objects.all()

class TipoUsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TipoUsuarioSeializer
    queryset = TipoUsuario.objects.all()

class UsuariosList(generics.ListAPIView):
    serializer_class = UsuariosSeializer
    queryset = Usuarios.objects.all()

class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuariosSeializer
    queryset = Usuarios.objects.all()

class IngreMalParqueadoList(generics.ListAPIView):
    serializer_class = IngreMalParqueadoSeializer
    queryset = IngreMalParqueado.objects.all()

class IngreMalParqueadoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IngreMalParqueadoSeializer
    queryset = IngreMalParqueado.objects.all()

class CalificacionList(generics.ListAPIView):
    serializer_class = CalificacionSeializer
    queryset = Calificacion.objects.all()

class CalificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CalificacionSeializer
    queryset = Calificacion.objects.all()