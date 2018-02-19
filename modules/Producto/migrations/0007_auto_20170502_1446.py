# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0006_detalleproducto_especificaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentacion',
            name='contenido',
            field=models.CharField(default='contenido', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentacion',
            name='empaque',
            field=models.CharField(default='empaque', max_length=100),
            preserve_default=False,
        ),
    ]