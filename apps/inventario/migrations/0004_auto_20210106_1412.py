# Generated by Django 2.2.4 on 2021-01-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20201124_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='fechalimite',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
