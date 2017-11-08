# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_auto_20170909_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuracionServicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meses', models.IntegerField(verbose_name='Cantidad de Meses')),
            ],
            options={
                'verbose_name': 'Duracion del Servicio',
                'verbose_name_plural': 'Duraciones de los Servicios',
            },
        ),
        migrations.AlterField(
            model_name='servicios',
            name='duracion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.DuracionServicios', verbose_name='Tiempo del contrato'),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='precio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio del Servicio'),
        ),
    ]
