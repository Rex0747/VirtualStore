from django.shortcuts import render
from articulos.models import articulos
from proveedores.models import proveedores
from agencias.models import agencias
from entradas.models import entradas
from _datetime import datetime
from django.http import HttpResponse

# Create your views here.
def addEntrada(request):
    nalbaran='';unidades='';referencia='';precunidad='';peso='';proveedor='';
    agencia='';precporte='';portepag='';error=False

    if request.method == 'POST':
        if request.POST['nalbaran']:
            nalbaran = request.POST['nalbaran']
            print(nalbaran)
        else:
            error=True
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
            proveedor = request.POST['proveedor']
            print(proveedor)
        if request.POST['agencia']:
            agencia = request.POST['agencia']
            print(agencia)
        if request.POST['precporte']:
            precporte = request.POST['precporte']
            print(precporte)
        if request.POST['portepag']:
            portepag = request.POST['portepag']
            print(str(portepag))

    if error==True:
        agencia = agencias.objects.all()
        proveedor = proveedores.objects.all()
        return render(request, 'addentrada.html',{'agencia': agencia, 'proveedor': proveedor})

    print('Agencia: ' + str(agencia))
    print('Proveedor: ' + str(proveedor))
    fecha = datetime.now()

    data=entradas(nAlbaran=nalbaran,fk_proveedor=int(proveedor),fk_articulo=referencia,FechaEntrada=fecha,
    Unidades=unidades,PrecioUnidad=precunidad,Peso=peso,Agencia=int(agencia),PrecioPorte=precporte,porte_pagado=str(portepag))

    return render( request, 'addentrada.html')

