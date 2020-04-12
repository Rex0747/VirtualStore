from django.shortcuts import render
from tiendainf.excel import Excell
from virtualstore.settings import MEDIA_ROOT
from django.http import HttpResponse
from articulos.models import articulos , familia
from proveedores.models import proveedores
# Create your views here.

def ImportarArticulos(request):
    excel = None
    #try:
    excel = Excell( MEDIA_ROOT +'\\xlsx\\' + 'articulos.xlsx' )
    nfilas = str( excel.getnumerofilas() -1 )
    fila = excel.leer_fichero()
    print( 'Numero de lineas: ' + str( nfilas) )
    for item in fila:
        #print(str(item))
        idFam=familia.objects.filter(codigo=item[2])
        idProv=proveedores.objects.get(codProveedor=item[4])
        ref=articulos(codigo=item[0],nombre=item[1],familia=idFam.first(),fabricante=item[3],proveedor_id=idProv.pk,
                      precio=item[5],codbarras=item[6],codqr=item[7],imagen=item[8])
        ref.save()
    #except Exception as e:
        #return HttpResponse('<p>'+str(e)+'</p>')
    return HttpResponse('<p>'+str(fila)+'</p>')





