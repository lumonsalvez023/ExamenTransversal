from django.urls import path
from .views import listarProducto, catalogo, agregarProducto, modificarProducto, eliminarProducto

urlpatterns = [
    path('',listarProducto, name='listarProducto'),
    path('catalogo/',catalogo, name='catalogo'),
    path('agregarProducto/',agregarProducto,name='agregarProducto'),
    path('editar/<int:id_producto>',modificarProducto,name='modificar_producto'),
    path('eliminar/<int:id_producto>',eliminarProducto, name='eliminar_producto')
]