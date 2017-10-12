from django.contrib.auth.models import User
from django.db import models


SEXO =(("Masculino", "Masculino"),("Femenino", "Femenino"))
ENTRADA_SALIDA =(("0", "Entrada"),("1", "Salida"))


class Marcacione(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=200)
    estado = models.CharField(max_length=40, choices=ENTRADA_SALIDA, blank=True, null=True)
    latitud = models.CharField(max_length=200, blank=True, null=True)
    longitud = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.CharField(max_length=100,null=True, blank=True)
    hora = models.CharField(max_length=100,null=True, blank=True)
    observaciones = models.CharField(max_length=150, null=True, blank=True)
    device_id = models.CharField(max_length=200, null=True, blank=True)
    zona = models.CharField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
    def __str__(self):
        return str(self.usuario)


class JefeSupermercado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
	
    def __str__(self):
        return str(self.usuario)
	
class Perfile(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    telefono_id = models.CharField(max_length=40, blank=True, null=True)
    sexo = models.CharField(max_length=40, choices=SEXO, blank=True, null=True)
    legajo = models.CharField(max_length=40, blank=True, null=True)
    jefe = models.ForeignKey(JefeSupermercado, on_delete=models.CASCADE, blank=True, null=True)
    esta_activo = models.BooleanField(default=False)
	
    def __str__(self):
        return str(self.usuario)
	
class Usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    telefono_id = models.CharField(max_length=40, blank=True, null=True)
    sexo = models.CharField(max_length=40, choices=SEXO, blank=True, null=True)
    legajo = models.CharField(max_length=40, blank=True, null=True)
    esta_activo = models.BooleanField(default=False)
	
    def __str__(self):
        return str(self.usuario)