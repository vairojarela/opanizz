# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-04 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0017_servicios_precio_beneficiario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duracionservicios',
            name='nombre',
            field=models.CharField(max_length=20, null=True, verbose_name='Cantidad de Tiempo'),
        ),
        migrations.RemoveField(
            model_name='servicios',
            name='duracion',
        ),
        migrations.AddField(
            model_name='servicios',
            name='duracion',
            field=models.ManyToManyField(null=True, to='administracion.DuracionServicios', verbose_name='Duraciones posibles del servicio'),
        ),
    ]
