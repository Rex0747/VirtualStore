from django.db import models
from _datetime import datetime

# Create your models here.
class salidas(models.Model):
    codigo = models.CharField(max_length=8, null=False)
    fechaSalida = models.DateTimeField(default=datetime.now, blank=True)
    unidades = models.IntegerField(null=False)
    precioUnidad = models.FloatField(null=False)
    agencia = models.CharField(max_length=20, null=True)
    precioPorte = models.FloatField(null=True)
    enviado=models.BooleanField(null=False)

    def __str__(self):
        return '%s %s %s %s %s %s %s' % ( self.codigo, self.fechaSalida, self.unidades, self.precioUnidad,
                                          self.agencia, self.precioPorte, self.enviado )

