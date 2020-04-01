from django.db import models

# Create your models here.

class articulos(models.Model):
    codigo=models.CharField(max_length=8, null=False)
    nombre=models.CharField(max_length=70, null=False)
    fabricante=models.CharField(max_length=20, null=False)
    proveedor=models.CharField(max_length=20, null=True)
    codbarras=models.CharField(max_length=50, null=False,default='')
    codqr=models.CharField(max_length=255, null=False,default='')
    precio=models.FloatField(default=0)
    familia=models.ForeignKey('familia', on_delete=models.CASCADE)
    imagen=models.ImageField(max_length=50,null=False,default='')

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s' %(self.codigo, self.nombre, self.fabricante, self.proveedor,
            self.codbarras, self.codqr, self.codbarras, self.precio, self.familia, self.imagen)

    class Meta:
    #    constraints = [
    #    models.UniqueConstraint( fields=['codigo', 'fabricante'] )
        unique_together = ('codigo','fabricante')
    #    ]

class familia(models.Model):
    codigo=models.CharField(max_length=25, unique=True )        #repuestos , equipos , accesorios , herramientas , software
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' %(self.codigo, self.nombre)





