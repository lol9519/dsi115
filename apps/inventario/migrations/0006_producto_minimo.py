# Generated by Django 2.2.7 on 2021-01-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_auto_20210105_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='minimo',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
