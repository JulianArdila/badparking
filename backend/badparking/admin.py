from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(TipoUsuario)
admin.site.register(Usuarios)
admin.site.register(IngreMalParqueado)
admin.site.register(Calificacion)