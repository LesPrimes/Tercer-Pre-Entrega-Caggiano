from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    #_____________________Formularios
    path("articulos/", ArticuloCreate.as_view() , name="articulos"),
    path("escritor/", EscritorCreate.as_view() ,name="escritores"),
    path("lector/", LectorCreate.as_view(), name="lectores"),
    #___________________Busqueda
    path("buscar_articulos", buscar_articulos, name ="buscar_articulos"),
    path("encontrar_articulos", encontrar_articulos, name = "encontrar_articulos")
]