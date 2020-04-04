from django.contrib import admin
from articulos.models import articulos, familia
from clientes.models import clientes
from entradas.models import entradas
from salidas.models import salidas
from proveedores.models import proveedores
from agencias.models import agencias


# Register your models here.

class entradasclas(admin.ModelAdmin):
    list_display = ('nAlbaran', 'fechaEntrada', 'unidades', 'precioUnidad', 'agencia', 'precioPorte')
    search_fields = ('codigo', 'fechaEntrada')
    list_filter = ('fechaEntrada',)

admin.site.register( articulos )
admin.site.register( clientes )
admin.site.register( entradas, entradasclas)
admin.site.register( salidas )
admin.site.register( proveedores )
admin.site.register( familia )
admin.site.register( agencias )