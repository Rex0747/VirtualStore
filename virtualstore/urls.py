"""virtualstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from clientes import views as viewClient
from entradas import views as viewEntradas
from salidas import views as viewSalidas
from tiendainf import views as viewTienda
from articulos import views as viewArticulos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('addclient', viewClient.AddCliente),
    path('addsalida',viewSalidas.AddSalida),
    path('virtualstore', viewTienda.virtualstore),
    path('p/<url>', viewTienda.portatiles),
    path('addentrada',viewEntradas.addEntrada),
    path('imparticulos/',viewArticulos.ImportarArticulos),





]   #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
