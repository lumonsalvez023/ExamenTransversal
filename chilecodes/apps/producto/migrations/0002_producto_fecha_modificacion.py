# Generated by Django 3.1.4 on 2020-12-14 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
