from django.db import models
from _datetime import datetime
# Create your models here.

class agencias(models.Model):
    codAgencia=models.CharField(max_length=8,blank=False)
    nombre=models.CharField(max_length=40,blank=False)
    direccion=models.CharField(max_length=30,blank=False,default='')
    cp=models.CharField(max_length=5,default='',blank=True)
    telefono=models.CharField(max_length=9,blank=True,default='')
    movil=models.CharField(max_length=9,blank=True,default='')
    mail = models.EmailField(blank=True)

    def __str__(self):
        return '%s %s %s %s %s %s %s' %(self.codAgencia,self.nombre,self.direccion,self.cp,
                                             self.telefono,self.movil,self.mail)