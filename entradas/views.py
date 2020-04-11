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
    agencia='';_agencia='';precporte='';portepag=False;error=False;_agencia='';_proveedor='';

    if request.method == 'POST':
        if request.POST['nalbaran']:
            nalbaran = request.POST['nalbaran']
            print(nalbaran)
        if request.POST['ref']:
            referencia = request.POST['ref']
        else:
            error=True
        if request.POST['unidades']:
            unidades = request.POST['unidades']
        else:
            error=True
        if request.POST['precunid']:
            precunidad = request.POST['precunid']
        else:
            error=True
        if request.POST['peso']:
            peso = request.POST['peso']
        else:
            error=True
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


    if error==True or request.method != 'POST':
        agencia = agencias.objects.all()
        proveedor = proveedores.objects.all()
        return render(request, 'addentrada.html',{'agencia': agencia, 'proveedor': proveedor})

    try:
        _agencia=agencias.objects.filter(id=agencia)
        _proveedor=proveedores.objects.filter(id=proveedor)
    except Exception as e:
        print('Excepcion al canto: '+ str( e))

    print('Agencia: ' + str(_agencia))
    print('Proveedor: ' + str(_proveedor))
    fecha = datetime.now()
    #from django.db import connection
    #print(connection.queries)
    if nalbaran == '' :
        nalbaran=entradas.objects.latest('id')
        print('nalbaran: '+ str(nalbaran))
        nalbaran = str( int( nalbaran.nAlbaran ) +  1 )
        print('nalbaran: '+ nalbaran )

    try:
        _referencia=articulos.objects.filter(codigo=referencia)

        data=entradas(nAlbaran=nalbaran,fk_proveedor=_proveedor.get(id=proveedor) ,fk_articulo=_referencia.get(codigo=referencia),fechaEntrada=fecha,
        unidades=unidades,precioUnidad=precunidad,peso=peso,agencia=_agencia.get(id=agencia),precioPorte=precporte,porte_pagado=str(portepag))
        data.save()
    except Exception as e:
        print('ERROR: '+ str(e))
    agencia = agencias.objects.all()
    proveedor = proveedores.objects.all()
    return render( request, 'addentrada.html',{'agencia': agencia, 'proveedor': proveedor} )

