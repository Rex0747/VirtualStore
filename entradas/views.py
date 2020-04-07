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
    agencia='';_agencia='';precporte='';portepag=False;error=False

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
        if 'portepag' in request.POST:
            portepag = request.POST['portepag']
            print(str(portepag))
            if portepag == 'on':
                portepag=True
        else:
            portepag=False

    if error==True:
        agencia = agencias.objects.all()
        proveedor = proveedores.objects.all()
        return render(request, 'addentrada.html',{'agencia': agencia, 'proveedor': proveedor})

    _agencia=agencias.objects.filter(id=agencia)
    _proveedor=proveedores.objects.filter(id=proveedor)

    print('Agencia: ' + str(_agencia))
    print('Proveedor: ' + str(proveedor))
    fecha = datetime.now()
    #from django.db import connection
    #print(connection.queries)
    

    data=entradas(nAlbaran=nalbaran,fk_proveedor=_proveedor.get(id=proveedor) ,fk_articulo=referencia,fechaEntrada=fecha,
    unidades=unidades,precioUnidad=precunidad,peso=peso,agencia=_agencia.get(id=agencia),precioPorte=precporte,porte_pagado=str(portepag))
    data.save()

    agencia = agencias.objects.all()
    proveedor = proveedores.objects.all()
    return render( request, 'addentrada.html',{'agencia': agencia, 'proveedor': proveedor} )

