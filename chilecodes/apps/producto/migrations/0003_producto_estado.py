# Generated by Django 3.1.4 on 2020-12-17 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto_fecha_modificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Exite/No Existe'),
        ),
    ]