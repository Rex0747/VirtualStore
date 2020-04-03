from django.db import models
from _datetime import datetime

# Create your models here.
class clientes(models.Model):
    codigo = models.CharField(max_length=6, unique=True, null=False)
    cliente = models.CharField(max_length=60, null=False)
    direccion = models.CharField(max_length=60, null=True)
    cp = models.CharField(max_length=5, null=True)
    telefono = models.CharField(max_length=9, null=True)
    movil = models.CharField(max_length=9, null=True)
    mail=models.EmailField(max_length=60, unique=True, null=True)
    fecha_alta=models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return'%s %s %s %s %s %s %s %s' %(self.codigo,self.cliente,self.direccion,
        self.cp,self.telefono,self.movil,self.mail,self.fecha_alta)









