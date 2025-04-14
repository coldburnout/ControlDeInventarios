from django.contrib import admin
from .models import Producto, Orden
from django.contrib.auth.models import Group

admin.site.site_header = "Control de Inventario"

class administradorDeProductos(admin.ModelAdmin):
    list_display = ('nombre','categoria','cantidad',)
    list_filter = ('categoria',)

# Register your models here.
admin.site.register(Producto, administradorDeProductos)
admin.site.register(Orden)
#admin.site.unregister(Group)