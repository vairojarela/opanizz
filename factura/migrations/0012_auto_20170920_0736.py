# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 11:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0011_auto_20170920_0728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura',
            options={'verbose_name': 'Factura', 'verbose_name_plural': 'Datos de la Facturacion'},
        ),
    ]