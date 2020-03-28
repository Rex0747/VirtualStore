from django.shortcuts import render

# Create your views here.
def AddEntrada(request):

    return render( request, 'entradas.html')
