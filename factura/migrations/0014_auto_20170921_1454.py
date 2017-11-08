# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-21 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0013_auto_20170920_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='base_imponible',
            field=models.FloatField(blank=True, null=True, verbose_name='Base Imponible de la Factura'),
        ),
        migrations.AddField(
            model_name='factura',
            name='iva',
            field=models.FloatField(blank=True, null=True, verbose_name='IVA de la Factura'),
        ),
        migrations.AddField(
            model_name='factura',
            name='total',
            field=models.FloatField(blank=True, null=True, verbose_name='Total de la Factura'),
        ),
    ]
