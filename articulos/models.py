from django.db import models

# Create your models here.
class articulos(models.Model):
    codigo=models.CharField(max_length=8, null=False)
    nombre=models.CharField(max_length=70, null=False)
    fabricante=models.CharField(max_length=20, null=True)
    proveedor=models.CharField(max_length=20, null=True)
    codbarras=models.CharField(max_length=50, null=True)
    codqr=models.CharField(max_length=255, null=True)
    precio=models.IntegerField(default=0)
    familia=models.ForeignKey('familia', on_delete=models.CASCADE)


class familia(models.Model):
    tipo=models.CharField(max_length=25)       #repuestos , equipos , accesorios , herramientas , software


class tipos(models.Model):
    repuestos=models.CharField(max_length=60)   # piezas de repuesto basicas. resistencias condensadores circuitos etc
    equipos=models.CharField(max_length=60)
    accesorios=models.CharField(max_length=60)
    herramientas=models.CharField(max_length=60)
    software=models.CharField(max_length=60)
    hardware=models.CharField(max_length=60)    #placas micros memorias etc todolo que esta dentro de una cpu



