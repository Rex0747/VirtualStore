from django.shortcuts import render
from articulos.models import articulos

# Create your views here.
def virtualstore(request):


    return render(request, 'index.html',{'titulo': 'VIRTUALSTORE'} )

def portatiles(request, url):

    elemento=articulos.objects.all()





    return render(request, 'index.html', {'titulo': url,'elemento': elemento})
