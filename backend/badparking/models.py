from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField(auto_now_add=True)
    correo = models.CharField(max_length=150)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length=60)
    clave = models.CharField(max_length=60)
    tipo = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class IngreMalParqueado(models.Model):
    foto_ubicacion = models.CharField(max_length=300)
    latitud = models.CharField(max_length=60)
    longitud = models.CharField(max_length=60)
    fecha_de_registro = models.DateField()
    hora_de_registro = models.TimeField()
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    placa = models.CharField(max_length=20)
    confiden = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    valor = models.IntegerField()
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    ingreso_mal_parqueado = models.ForeignKey(IngreMalParqueado,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
