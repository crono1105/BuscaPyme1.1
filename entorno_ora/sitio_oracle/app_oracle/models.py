from io import open_code
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.
class clientePyme(models.Model):
    nomCliente=models.CharField(max_length=25)
    apellcliente=models.CharField(max_length=25)
    usuario=models.CharField(max_length=25)
    correo=models.TextField(max_length=40)
    fnacimiento=models.DateField(auto_now=False)
    contraseña=models.TextField(max_length=35)
    rut=models.CharField(max_length=10,primary_key=True)

    def __str__(self):
        return  self.rut


class Producto(models.Model):
    codigo=models.CharField(max_length=10,primary_key=True)
    descripcion=models.CharField(max_length=25)
    precio=models.IntegerField(default=0)

    def __str__(self):
        return  self.codigo + " " + self.descripcion

        
class categoria(models.Model):
    nomCategoria=models.CharField(max_length=60)
    idcategoria=models.CharField(max_length=10,primary_key=True)

    def __str__(self):
        return self.idcategoria


class pyme(models.Model):
    NomPyme=models.CharField(max_length=60)
    rutempresa=models.CharField(max_length=10,primary_key=True)
    direccion=models.CharField(max_length=25)
    rutpersona=models.CharField(max_length=10,)
    nomDueño=models.CharField(max_length=60)
    categpyme=models.CharField(max_length=25)
    horario=models.CharField(max_length=25)
    telefono=models.CharField(max_length=25)
   

    def __str__(self):
        return self.rutempresa


class usuarioApp(models.Model):
    nomuser=models.CharField(max_length=25)
    apelluser=models.CharField(max_length=25)
    usuario=models.CharField(max_length=25)
    correo=models.TextField(max_length=40)
    fnacimiento=models.DateField(auto_now=False)
    contraseña=models.TextField(max_length=35)
    rut=models.CharField(max_length=10,primary_key=True)

    def __str__(self):
        return  self.rut




