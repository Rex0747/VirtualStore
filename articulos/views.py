from django.shortcuts import render
from tiendainf.excel import Excell
from virtualstore.settings import MEDIA_ROOT
from django.http import HttpResponse
# Create your views here.

def ImportarArticulos(request):

    excel = None
    try:
        excel = Excell( MEDIA_ROOT +'\\xlsx\\' + 'articulos.xlsx' )
        nfilas = str( excel.getnumerofilas() -1 )
        fila = excel.leer_fichero()
        print( 'Numero de lineas: ' + str( nfilas) )
        for item in fila:
            for i in item:
                #print(str(i))
                print(str(item[0]))
                print(str(item[1]))
                print(str(item[3]))
                print(str(item[5]))

    except Exception as e:
        return HttpResponse('<p>'+str(e)+'</p>')

    return HttpResponse('<p>'+str(fila)+'</p>')


