# Generated by Django 2.2.7 on 2021-01-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20201124_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='nombreRepresentante',
            field=models.CharField(default='hola', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telefonoPersonal',
            field=models.CharField(default='adios', max_length=8),
            preserve_default=False,
        ),
    ]
