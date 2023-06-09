from django.shortcuts import render, redirect

from compra.models import Proveedor, Producto

# Create your views here.

def agregar_proveedor(request):
    """
    Agrega un nuevo proveedor a la base de datos.
    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
    Returns:
        HttpResponse: Redirige al listado de proveedores o renderiza el formulario para agregar un proveedor.
    """
    if request.POST:
        prov_nombr = request.POST['Nombre']
        prov_apellido = request.POST['Apellido']
        prov_dni = request.POST['DNI']

        Proveedor.objects.create(
            prov_nombre = prov_nombr,
			prov_apellido = prov_apellido,
            prov_dni = prov_dni,
        )

        return redirect('listado_proveedores')
    return render(request, 'agregar_proveedor.html')

def listado_proveedores(request):
    """Lista todos los registros de proveedores de la base de datos

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Renderiza el template en formato de tabla.
    """
    proveedores = Proveedor.objects.all()
    context= {
        'proveedores':proveedores
        }
    
    return render(request, 'listado_proveedores.html', context)

def agregar_producto(request):
    """
    Agrega un nuevo producto a la base de datos.
    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
    Returns:
        HttpResponse: Redirige al listado de productos o renderiza el formulario para agregar un producto.
    """
    proveedores = Proveedor.objects.all()
    context= {
        'proveedores':proveedores
    }
    if request.POST:
        prod_nombre = request.POST['Nombre']
        prod_precio  = request.POST['Precio']
        prod_stock_act = request.POST['Stock_actual']
        prod_proveedor_id= request.POST['Proveedor']

        Producto.objects.create(
            prod_nombre = prod_nombre,
			prod_precio = prod_precio,
            prod_stock_act = prod_stock_act,
            prod_proveedor_id = prod_proveedor_id
        )
        return redirect('listado_productos')

    return render(request, 'agregar_producto.html',context)    

def listado_productos(request):
    """Lista todos los registros de productos de la base de datos

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Renderiza el template en formato de tabla.
    """
    productos = Producto.objects.all()
    context= {
        'productos':productos
        }
    
    return render(request, 'listado_productos.html', context)