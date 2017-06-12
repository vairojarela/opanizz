# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-11 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contratos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('num_fact', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero de Factura')),
                ('fac_to', models.BooleanField(default=False, help_text='Se tomaran los datos del Cliente para Facturar', verbose_name='Facturar a nombre del Cliente')),
                ('fac_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre o Razon Social')),
                ('fac_rif', models.CharField(blank=True, max_length=15, verbose_name='R.I.F')),
                ('dir_fac', models.CharField(blank=True, max_length=150, verbose_name='Direccion Fiscal')),
                ('fac_tlf', models.IntegerField(blank=True, null=True, verbose_name='Telefono de Habitacion')),
                ('fac_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.Contratado', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Dato',
                'verbose_name_plural': 'Datos de Facturacion',
            },
        ),
    ]
