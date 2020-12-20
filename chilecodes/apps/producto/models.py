from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=45,null=False,blank=False)
    precio = models.PositiveIntegerField()
    imagen = models.FileField(upload_to='fotos')
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField('Exite/No Existe', default = True)