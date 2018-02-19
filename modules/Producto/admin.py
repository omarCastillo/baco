from django.contrib import admin
from .models import *

class coloresAdmin(admin.ModelAdmin):
  list_display = ('nombre','clave')
  search_fields = ['nombre','clave']

class productoAdmin(admin.ModelAdmin):
  list_display = ('nombre',)
  search_fields = ['nombre',]

class subproductoAdmin(admin.ModelAdmin):
  list_display = ('nombre','producto')
  list_display_links = ['producto',]
  list_editable = ['nombre',]
  search_fields = ['nombre',]

class detalleproductoAdmin(admin.ModelAdmin):
  list_display = ('nombre','clave')
  search_fields = ['nombre','clave']

# Register your models here.
admin.site.register(Linea)
admin.site.register(Producto, productoAdmin)
admin.site.register(SubProducto, subproductoAdmin)
admin.site.register(Presentacion)
admin.site.register(Color, coloresAdmin)
admin.site.register(DetalleProducto, detalleproductoAdmin)