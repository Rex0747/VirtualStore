from django.db import models
from _datetime import datetime

from django.forms import FloatField

from articulos.models import articulos
from clientes.models import clientes

# Create your models here.
class entradas(models.Model):
    fk_cliente=models.ForeignKey(clientes, on_delete=models.CASCADE,default=1)
    codigo=models.CharField(max_length=8,null=False, verbose_name='codigo')
    #fk_articulo=models.ForeignKey(articulos,on_delete=models.CASCADE,blank=True)
    #nombre=models.CharField(max_length=70,null=True)
    fechaEntrada=models.DateTimeField(default=datetime.now, blank=True)
    unidades=models.IntegerField(null=False)
    precioUnidad=models.FloatField(null=False)
    peso=models.FloatField( default=0)
    agencia=models.CharField(max_length=20, null=True,default='')
    precioPorte=models.FloatField(null=True,default=True)
    porte_pagado=models.NullBooleanField(default=True)
    #precioTotal= models.FloatField(default=0)


    def __str__(self):
        print(type(entradas.precioUnidad))
        #precTotal = (entradas.precioUnidad * entradas.unidades)

        #if(entradas.porte_pagado==False):
            #precTotal=precTotal+entradas.precioPorte
        #entradas.precioTotal=precTotal

        return '%s %s %s %s %s %s %s %s %s' % (self.fk_cliente, self.codigo, self.fechaEntrada, self.unidades, self.precioUnidad,
                                          self.peso, self.agencia, self.precioPorte,self.porte_pagado )
    class META:
        ordering=['fechaEntrada']

