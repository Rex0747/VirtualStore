from django.shortcuts import render
from articulos.models import articulos

# Create your views here.
def virtualstore(request):


    return render(request, 'index.html',{'titulo': 'VIRTUALSTORE'} )

def portatiles(request, url):
    contenedor = []; col1=[]; col2=[]; col3=[];
    elemento=articulos.objects.all() #[:21]
    columna=0
    for i in elemento:
        if columna == 0:
            col1.append(i)
        if columna == 1:
            col2.append(i)
        if columna == 2:
            col3.append(i)
        columna += 1
        if columna > 2:
            columna=0

    print('contenedor: ' + str( contenedor ))
    return render(request, 'index.html', {'titulo': url,'col1': col1,'col2': col2,'col3': col3})
