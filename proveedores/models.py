from django.db import models

# Create your models here.
class proveedores(models.Model):
    codigo=models.CharField(max_length=8, null=False)
    nombre=models.CharField(max_length=50, null=False)
    direccion=models.CharField(max_length=50, null=True)
    cp=models.CharField(max_length=5, null=True)
    telefono=models.CharField(max_length=9, null=True)
    movil=models.CharField(max_length=9, null=True)

    def __str__(self):
        return '%s %s %s %s %s %s' %(self.codigo,self.nombre,self.direccion,self.cp,self.telefono,self.movil)






