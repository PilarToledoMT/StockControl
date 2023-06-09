from django.db import models

# Create your models here.

class Proveedor(models.Model):
    """
    Modelo que representa a un proveedor.

    Este modelo se utiliza para almacenar información sobre los proveedores.
    Los proveedores tienen un nombre, apellido, y dni.
    """
    prov_nombre = models.CharField(max_length=100, verbose_name='Nombre')
    prov_apellido = models.CharField(max_length=100, verbose_name='Apellido')
    prov_dni = models.IntegerField(verbose_name='DNI')

    def __str__(self):
        return f"""
        Nombre: {self.prov_nombre}
        Apellido: {self.prov_apellido}
        DNI: {self.prov_dni}."""

class Producto(models.Model):
    """
    Modelo que representa a un producto.

    Este modelo se utiliza para almacenar información sobre los productos.
    Los productos tienen un nombre, precio, stock_actual, y un proveedor.
    """
    prod_nombre = models.CharField(max_length=100, verbose_name='Nombre')
    prod_precio = models.FloatField(verbose_name='Precio')
    prod_stock_act= models.IntegerField(verbose_name='Stock_actual')
    prod_proveedor = models.ForeignKey(
        Proveedor, 
        related_name='proveedores',
        on_delete=models.CASCADE,
        verbose_name='Proveedor',
    )

    def __str__(self):
        return f"""
        Nombre: {self.prod_nombre}
        Precio: ${self.prod_precio}
        Stock actual: {self.prod_stock_act}
        Proveedor: {self.prod_proveedor}."""
