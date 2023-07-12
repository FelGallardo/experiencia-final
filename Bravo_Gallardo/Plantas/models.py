import datetime
from django.db import models

# Create your models here.

class Productos(models.Model):
    idprod                  = models.IntegerField(primary_key=True, verbose_name="idProduct")
    nombreproduc            = models.CharField(max_length=100, verbose_name="NombreProd")
    descripcion             = models.CharField(max_length=500, verbose_name="Descripcion")
    imagen                  = models.ImageField(upload_to="imagenes", null=True,blank=True, verbose_name="imagen")
    precio                  = models.IntegerField(verbose_name="Precio" )
    stock                   = models.IntegerField(verbose_name="Stock",default=0)
    
    def __str__(self):
        return self.nombreproduc


class Boleta(models.Model):
    id_boleta               = models.AutoField(primary_key=True)
    total                   = models.BigIntegerField()
    fecha_compra            = models.DateTimeField(blank=False, null=False, default= datetime.datetime.now)

    def __str__(self):
        return str(self.id_boleta)



class detalle_boleta(models.Model):
    id_boleta               = models.ForeignKey('Boleta',blank=True, on_delete=models.CASCADE)
    id_detalle_boleta       = models.AutoField(primary_key=True)
    id_producto             = models.ForeignKey('Productos', on_delete=models.CASCADE)
    cantidad                = models.IntegerField()
    subtotal                = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)