# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0002_auto_20170428_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleproducto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/detalle/'),
        ),
    ]
