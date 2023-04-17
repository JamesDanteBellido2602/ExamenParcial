from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import Product
from datetime import date

# Create your models here.
class datosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    #relación uno a uno con un modelo 
    nombreUsuario = models.CharField(max_length=32,default='ANOMIMO')
    apellidoUsuario = models.CharField(max_length=32,default='ANONIMO')
    emailUsuario = models.CharField(max_length=25,default='')
    userNameUsuario = models.CharField(max_length=15,default='')
    contrasenaUsuario = models.CharField(max_length=32,default='')
    rolUsuario = models.CharField(max_length=512,default='')
    numCelularUsuario = models.CharField(max_length=9)
    fechIngresoUsuario = models.DateField(default=date.today)  #dentro de la tablas SQl, hay un campo prefinido par fecha

#Class datosProducto(models.Model):
    #user = models.OneToOneField(Product,on_delete=models.CASCADE)
    #nombreProducto = models.CharField(max_length=32,default='PRODUCTO-GENERAL')
    #codigoProducto = models.CharField(max_length=10,blank=false)
    #precioCompraProducto = models.PositiveIntegerField(null=true)
    #precioVentaProducto = models.DecimalField(max_digits=5,decimal_places=2,null=true)
    #usuarioRegistroProducto = models.ForeingKey(userNameUsuario,null=false,blank=false)


