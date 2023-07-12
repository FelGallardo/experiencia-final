from django.urls import path
from .views import agregar_producto, eliminar_producto, generarBoleta, index, limpiar_producto, producto, nosotros, Api, registrar, crear,eliminar, modificar, restar_producto, tienda

urlpatterns=[
    path('', index, name="index"),
    path('producto/', producto, name="producto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('Api/', Api, name="Api"),
    path('registrar/', registrar , name="registrar"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar,name="eliminar" ),
    path('modificar/<id>', modificar,name="modificar"),
    path('tienda/',tienda, name="tienda"),
    path('tienda/',tienda, name="tienda"),

    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_producto, name="limpiar"),
]
