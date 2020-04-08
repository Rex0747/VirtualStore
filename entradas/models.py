from django.db import models
from _datetime import datetime

from django.forms import FloatField

from articulos.models import articulos
from clientes.models import clientes
from proveedores.models import proveedores
from agencias.models import agencias

# Create your models here.
class entradas(models.Model):
    nAlbaran=models.CharField(max_length=8,null=False, verbose_name='Albaran')
    fk_proveedor=models.ForeignKey(proveedores,on_delete=models.CASCADE,blank=True)
    fk_articulo=models.ForeignKey(articulos,on_delete=models.CASCADE,blank=True) #models.CharField(max_length=8,blank=True) #
    #nombre=models.CharField(max_length=70,null=True)
    fechaEntrada=models.DateTimeField(default=datetime.now, blank=True)
    unidades=models.IntegerField(blank=False)
    precioUnidad=models.FloatField(blank=False)
    peso=models.FloatField( default=0)
    agencia=models.ForeignKey(agencias,on_delete=models.CASCADE, blank=True,default='')
    precioPorte=models.FloatField(blank=True,default=True)
    porte_pagado=models.BooleanField(default=True)
    #precioTotal= models.FloatField(default=0)


    def __str__(self):
        print(type(entradas.precioUnidad))
        #precTotal = (entradas.precioUnidad * entradas.unidades)

        #if(entradas.porte_pagado==False):
            #precTotal=precTotal+entradas.precioPorte
        #entradas.precioTotal=precTotal

        return '%s %s %s %s %s %s %s %s %s %s' % ( self.nAlbaran,self.fk_articulo,self.fk_proveedor, self.fechaEntrada, self.unidades, self.precioUnidad,
                                          self.peso, self.agencia, self.precioPorte,self.porte_pagado )
    class META:
        ordering=['fechaEntrada']

