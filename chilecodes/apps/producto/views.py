from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def listarProducto(request):
    productos = Producto.objects.all()
    context = {
        'productos':productos
    }
    return render(
        request,
        'base/index.html',
        context
    )

@login_required
def catalogo(request):
    productos = Producto.objects.all()
    context = {
        'productos':productos
    }
    return render(
        request,
        'producto/catalogo.html',
        context
    )

def agregarProducto(request):
    formulario = ProductoForm()
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            nuevoFormulario = formulario.save(commit=False)
            nuevoFormulario.usuario = request.user
            nuevoFormulario.save()
            return redirect('/producto/catalogo/')
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'producto/agregarProducto.html',
        context
    )

def modificarProducto(request,id_producto):
    producotoEncontrado = Producto.objects.get(pk=id_producto)
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=producotoEncontrado)
        if formulario.is_valid():
            formulario.save()
            return redirect('/producto/catalogo')
    else:
        formulario = ProductoForm(instance=producotoEncontrado)
    context = {
        'titulo':'Modificar producto',
        'formulario':formulario
    }
    return render(
        request,
        'producto/modificarProducto.html',
        context
    )

def eliminarProducto(request,id_producto):
    productoEncontrado = Producto.objects.get(pk = id_producto)
    productoEncontrado.delete()
    return redirect('/producto/catalogo')