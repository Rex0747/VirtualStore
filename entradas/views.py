from django.shortcuts import render
from articulos.models import articulos
from proveedores.models import proveedores
from agencias.models import agencias
from entradas.models import entradas

# Create your views here.
def addEntrada(request):
    nalbaran='';unidades='';referencia='';precunidad='';peso='';proveedor='';agencia='';precporte='';portepag='';

    if request.method == 'POST':
        if request.POST['nalbaran']:
            nalbaran = request.POST['nalbaran']
            print(nalbaran)
        if request.POST['ref']:
            referencia = request.POST['ref']
            print(referencia)
        if request.POST['unidades']:
            unidades = request.POST['unidades']
            print(unidades)
        if request.POST['precunid']:
            precunidad = request.POST['precunid']
            print(precunidad)
        if request.POST['peso']:
            peso = request.POST['peso']
            print(peso)
        if request.POST['proveedor']:
            peso = request.POST['proveedor']
            print(proveedor)
        if request.POST['agencia']:
            peso = request.POST['agencia']
            print(agencia)
        if request.POST['precporte']:
            peso = request.POST['precporte']
            print(precporte)
        if request.POST['portepag']:
            peso = request.POST['portepag']
            print(str(portepag))

#    data=entradas(nAlbaran='',fk_proveedor='',fk_articulo='',FechaEntrada='',Unidades='',PrecioUnidad='',
#                  Peso='',Agencia='',PrecioPorte='',porte_pagado='')



    return render( request, 'addentrada.html')

