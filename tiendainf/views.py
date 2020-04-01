from django.shortcuts import render

# Create your views here.
def virtualstore(request):

    return render(request, 'index.html',{'titulo': 'VIRTUALSTORE'} )

def portatiles(request, url):
    print('URL: ' + url)
    if url=='portatiles':
        return render(request, 'index.html', {'titulo': 'PORTATILES'})
    if url=='pcs':
        return render(request, 'index.html', {'titulo': 'PCS'})
