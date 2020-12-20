from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class PerfilUser(models.Model):
    rut = models.CharField(max_length=45,null=False,blank=False)
    telefono = models.PositiveIntegerField()
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)