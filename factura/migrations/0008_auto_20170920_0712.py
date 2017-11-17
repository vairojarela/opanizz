# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0015_auto_20170920_0416'),
        ('factura', '0007_auto_20170920_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='fac_fecha',
            field=models.DateTimeField(verbose_name='Fecha de la Factura'),
        ),
        migrations.AddField(
            model_name='factura',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.Servicios', verbose_name='Servicio Contratado'),
        ),
    ]