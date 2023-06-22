from django.urls import path
from .views import index, producto, nosotros, Api, registrar, crear,eliminar, modificar

urlpatterns=[
    path('', index, name="index"),
    path('producto/', producto, name="producto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('Api/', Api, name="Api"),
    path('registrar/', registrar , name="registrar"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar,name="eliminar" ),
    path('modificar/<id>', modificar,name="modificar"),
]
