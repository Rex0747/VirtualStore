from django.shortcuts import render

# Create your views here.
def virtualstore(request):


    return render(request, 'index.html',{'titulo': 'VIRTUALSTORE'} )

def portatiles(request, url):


    return render(request, 'index.html', {'titulo': url})
