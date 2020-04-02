from django.shortcuts import render

# Create your views here.
def AddSalida( request ):

    return render( request , 'salidas.html')
