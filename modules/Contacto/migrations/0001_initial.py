# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=60)),
                ('mensaje', models.TextField()),
                ('mail_envio', models.EmailField(max_length=254)),
            ],
        ),
    ]
