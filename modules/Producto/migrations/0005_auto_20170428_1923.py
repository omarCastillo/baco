# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0004_auto_20170428_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleproducto',
            name='colores',
            field=models.ManyToManyField(blank=True, to='Producto.Color'),
        ),
        migrations.AlterField(
            model_name='detalleproducto',
            name='presentaciones',
            field=models.ManyToManyField(blank=True, to='Producto.Presentacion'),
        ),
        migrations.AlterField(
            model_name='detalleproducto',
            name='subproducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='Producto.SubProducto'),
        ),
    ]
