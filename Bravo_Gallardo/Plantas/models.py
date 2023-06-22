from django.db import models

# Create your models here.

class Productos(models.Model):
    idprod                  = models.IntegerField(primary_key=True, verbose_name="idProduct")
    nombreproduc            = models.CharField(max_length=100, verbose_name="NombreProd")
    descripcion             = models.CharField(max_length=500, verbose_name="Descripcion")
    imagen                  = models.ImageField(upload_to="imagenes", null=True,blank=True, verbose_name="imagen")
    precio                  = models.IntegerField(verbose_name="Precio" )
    
    def __str__(self):
        return self.nombreproduc
