# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-28 13:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0003_auto_20170627_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contratado',
            name='domicilio_laboral',
        ),
    ]