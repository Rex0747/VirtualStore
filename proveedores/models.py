from django.db import models

# Create your models here.
class proveedores(models.Model):
    codProveedor=models.CharField(max_length=8, null=False)
    nombre=models.CharField(max_length=40, null=False)
    direccion=models.CharField(max_length=50, null=True)
    cp=models.CharField(max_length=5, null=True)
    telefono=models.CharField(max_length=9, null=True)
    movil=models.CharField(max_length=9, null=True)
    mail=models.EmailField(null=True)

    def __str__(self):
        return '%s %s %s %s %s %s' %(self.codProveedor,self.nombre,self.direccion,self.cp,self.telefono,self.movil)






