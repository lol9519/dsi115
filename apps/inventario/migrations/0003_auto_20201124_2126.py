# Generated by Django 2.2.4 on 2020-11-25 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_cuenta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuenta',
            old_name='fecha',
            new_name='fechacreacion',
        ),
        migrations.AddField(
            model_name='cuenta',
            name='fechalimite',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='titulo',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
