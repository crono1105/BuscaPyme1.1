from app_oracle.models import Producto, categoria,clientePyme, pyme, usuarioApp
from django.contrib import admin

# Register your models here.
class AdmPersona(admin.ModelAdmin):
    list_display=["rut,nomcliente,apellcliente,correo,contraseña,usuario,fnacimiento"]

    class Meta:
        model=clientePyme

admin.site.register(clientePyme)

class admcategoria(admin.ModelAdmin):
    list_display=["nomCategoria,idcategoria"]

    class meta:
        model=categoria
admin.site.register(categoria)        


class admproducto(admin.ModelAdmin):
    list_display=["codigo,descripcion,precio"]

    class meta:
        model=Producto
admin.site.register(Producto)        


class admpyme(admin.ModelAdmin):
    list_display=["NomPyme,rutempresa,direccion,rutpersona,nomDueño,categpyme,horario,telefono"]

    class meta:
        model=pyme
admin.site.register(pyme)       


class admuserApp(admin.ModelAdmin):
    list_display=["nomuser,apelluser,usuario,correo,fnacimiento,contraseña,rut"]

    class meta:
        model=usuarioApp
admin.site.register(usuarioApp)        
