# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-08 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0020_auto_20171008_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratado',
            name='fecha_contratacion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contratado',
            name='fecha_expiracion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
