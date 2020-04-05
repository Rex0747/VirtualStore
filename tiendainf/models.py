from django.db import models
from articulos.models import articulos
from proveedores.models import proveedores

# Create your models here.


class ubicacionesStocks(models.Model):
    sala=models.CharField(max_length=10,blank=False)
    modulo=models.CharField(max_length=6,blank=False)
    estanteria=models.CharField(max_length=6,blank=False)
    ubicacion=models.CharField(max_length=6,blank=False)
    fk_articulo = models.ForeignKey(articulos, on_delete=models.CASCADE)
    stock=models.FloatField()


    def __str__(self):
        return '%s %s %s %s %s %s' % ( self.sala, self.modulo, self.estanteria, self.ubicacion,
                                          self.fk_articulo, self.stock )

