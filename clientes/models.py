from django.db import models
from _datetime import datetime

# Create your models here.
class clientes(models.Model):
    codigo = models.CharField(max_length=6, unique=True, null=False)
    roll=models.CharField(max_length=15, null=False)
    activo=models.IntegerField( null=False )
    nombre = models.CharField(max_length=60, null=False)
    direccion = models.CharField(max_length=60, null=True)
    mail=models.EmailField(max_length=60, unique=True, null=True)
    fecha_alta=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return'%s %s %s %s %s %s %s' %(self.codigo,self.roll,self.activo,self.nombre,self.direccion,self.mail,self.fecha_alta)









