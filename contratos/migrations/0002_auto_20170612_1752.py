# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-12 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratado',
            name='vivienda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='generalidades.Vivienda', verbose_name='Vivienda'),
        ),
    ]
