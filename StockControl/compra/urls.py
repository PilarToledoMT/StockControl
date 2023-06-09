from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/nuevo', views.agregar_proveedor, name = "agregar_proveedor"),
    path('proveedores/listado', views.listado_proveedores, name = "listado_proveedores"),

    path('productos/nuevo', views.agregar_producto, name = "agregar_producto"),
    path('productos/listado', views.listado_productos, name = "listado_productos"),
]