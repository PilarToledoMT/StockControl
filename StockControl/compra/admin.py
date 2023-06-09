from django.contrib import admin

from compra.models import Producto, Proveedor

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ['id', 'prod_nombre', 'prod_precio', 'prod_stock_act', 'prod_proveedor']
    search_fields = ['prod_nombre']
    list_filter = ['prod_proveedor__prov_apellido', 'prod_nombre']

class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = ['id', 'prov_nombre', 'prov_apellido', 'prov_dni']
    search_fields = ['prov_dni']
    list_filter = ['prov_apellido']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
