from django.shortcuts import render
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import CreateView


# Create your views here.


def home(request):
    return render(request,"aplicacion/index.html")

def articulos(request):
    return render(request,"aplicacion/articulo_.html")

def escritores(request):
    return render(request,"aplicacion/escritorForm.html")

def lectores(request):
    return render(request,"aplicacion/lectorForm.html")


#______________________________Formularios 

class ArticuloCreate(CreateView):
    model = Articulo
    fields = ["titulo","genero","fecha_de_publicacion"]
    success_url = reverse_lazy("articulos")

class LectorCreate(CreateView):
    model = Lector
    fields = ["nombre","apellido","email"]
    success_url = reverse_lazy("home")

class EscritorCreate(CreateView):
    model = Escritor
    fields = ["nombre","apellido","email"]
    success_url = reverse_lazy("home")
 
#__________________________Buscador de Articulos 
  
def buscar_articulos(request):
   return render(request, "aplicacion/buscar.html")

def encontrar_articulos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        articulos = Articulo.objects.filter(titulo__icontains=patron)
        contexto = {"articulos": articulos}
        return render(request,"aplicacion/articulos.html", contexto)
    else:
        contexto = {"articulos" : Articulo.objects.all()}
        return render(request,"aplicacion/articulos.html",contexto)