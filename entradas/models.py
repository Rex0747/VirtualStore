from django.db import models
from _datetime import datetime
from articulos.models import articulos

# Create your models here.
class entradas(models.Model):
    codigo=models.CharField(max_length=8,null=False, verbose_name='codigo')
    fk_articulo=models.ForeignKey(articulos,on_delete=models.CASCADE,blank=True)
    nombre=models.CharField(max_length=70,null=True)
    fechaEntrada=models.DateTimeField(default=datetime.now, blank=True)
    unidades=models.IntegerField(null=False)
    precioUnidad=models.FloatField(null=False)
    agencia=models.CharField(max_length=20, null=True)
    precioPorte=models.FloatField(null=True)

    def __str__(self):
        nombre=articulos.objects.get( id=1 )
        print('Articuño: '+str(nombre))
        return '%s %s %s %s %s %s %s' % ( self.codigo,self.nombre, self.fechaEntrada, self.unidades, self.precioUnidad,
                                          self.agencia, self.precioPorte )
    class META:
        ordering=['fechaEntrada']

