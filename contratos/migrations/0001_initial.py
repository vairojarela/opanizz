# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 12:30
from __future__ import unicode_literals

import contratos.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('generalidades', '0001_initial'),
        ('clientes', '0001_initial'),
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('cedula', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('fecha_n', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('telefono', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Beneficiario',
                'verbose_name_plural': 'Beneficiarios',
            },
        ),
        migrations.CreateModel(
            name='Contratado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numcontrato', models.CharField(default=contratos.models.incremental, editable=False, max_length=20)),
                ('cedula', models.IntegerField(unique=True)),
                ('edad', models.IntegerField(null=True)),
                ('fecha_n', models.DateField(blank=True, verbose_name='Fecha de Nacimiento')),
                ('rif', models.CharField(blank=True, help_text='Opcional si posee', max_length=15, verbose_name='R.I.F.')),
                ('telefono_o', models.IntegerField(null=True, verbose_name='Telefono Oficina')),
                ('nombre_sector', models.CharField(blank=True, max_length=50, verbose_name='Nombre del Sector')),
                ('nombre_ubicacion', models.CharField(blank=True, max_length=60, verbose_name='Nombre de la Ubicacion')),
                ('nombre_vivienda', models.CharField(blank=True, max_length=100, verbose_name='Nombre de la Vivienda')),
                ('piso', models.CharField(blank=True, max_length=10)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('domicilio_laboral', models.CharField(blank=True, max_length=200)),
                ('punto_referencia', models.CharField(blank=True, max_length=250, verbose_name='Punto de Referencia de busqueda')),
                ('cancer', models.CharField(blank=True, max_length=20, verbose_name='Cancer')),
                ('diabetes', models.CharField(blank=True, max_length=20, verbose_name='Diabetes')),
                ('enfermedad_corazon', models.CharField(blank=True, max_length=20, verbose_name='Enfermedades del Corazon')),
                ('presion_arterial', models.CharField(blank=True, max_length=20, verbose_name='Presion Arterial Alta')),
                ('enfermedad_renal', models.CharField(blank=True, max_length=20, verbose_name='Enfermedades Renales')),
                ('enfermendad_mental', models.CharField(blank=True, max_length=20, verbose_name='Enfermedades Mentales')),
                ('enfermedades_importantes', models.CharField(blank=True, max_length=250, verbose_name='Otras Importantes')),
                ('salud', models.CharField(blank=True, choices=[('Buena', 'Buena'), ('Regular', 'Regular'), ('Mala', 'Mala')], max_length=7, verbose_name='Estado de Salud')),
                ('peso', models.CharField(blank=True, max_length=4, verbose_name='Indique su peso')),
                ('estatura', models.CharField(blank=True, max_length=5, verbose_name='Indique su Estatura')),
                ('enfermedad_respiratoria', models.CharField(blank=True, choices=[('Bronquitis', 'Bronquietes Cronica'), ('Tuberculosis', 'Tuberculosis'), ('Asma', 'Asma'), ('Otras', 'Otras')], help_text='Indique si Padece', max_length=50, verbose_name='Enfermedades Respiratorias')),
                ('indique_respiratoria', models.CharField(blank=True, help_text='Especifique enfermedad Respirarotia', max_length=150, verbose_name='Indique')),
                ('enfermedad_digestivo', models.CharField(blank=True, choices=[('Enfermedades del higado', 'Enfermedades del higado'), ('Ulcera gastroduodenal', 'Ulcera gastroduodenal'), ('Dispepcia', 'Dispepcia'), ('Gastritis', 'Gastritis'), ('Otras enfermedades', 'Otras enfermedades')], help_text='Indique si Padece', max_length=50, verbose_name='Enfermedades Digestivas')),
                ('indique_digestivo', models.CharField(blank=True, help_text='Especifique Enfermedad Digestiva', max_length=150, verbose_name='Indique')),
                ('enfermedad_circulatorio', models.CharField(blank=True, choices=[('Trastorno en la presion arterial', 'Trastorno en la presion arterial '), ('Alteraciones cardiacas', 'Alteraciones cardiacas'), ('Angina de pecho', 'Angina de pecho '), ('Infarto de miocardio', 'Infarto de miocardio'), ('Otras enfermedades relacionados', 'Otras enfermedades relacionados:')], help_text='Indique si Padece', max_length=50, verbose_name='Enfermedades Circulatorias')),
                ('indique_circulatorio', models.CharField(blank=True, help_text='Especifique Enfermedad Circulatoria', max_length=150, verbose_name='Indique')),
                ('otras_enfermedades', models.CharField(blank=True, choices=[('Reumatismo', 'Reumatismo'), ('Artritis', 'Artritis'), ('Hemorragias de cualquier indole', 'Hemorragias de cualquier indole'), ('Perdida del conocimiento', 'Perdida del conocimiento'), ('Enfermedades en los huesos', 'Enfermedades en los huesos'), ('Convulsiones', 'Convulsiones'), ('Paralisis', 'Paralisis')], help_text='Indique si Padece', max_length=50, verbose_name='Otras Enfermedades')),
                ('indique_otras', models.CharField(help_text='Especifique la enfermedad', max_length=150, verbose_name='Indique')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Potenciales')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generalidades.Estado', verbose_name='Estado')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generalidades.Municipio', verbose_name='Municipio')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generalidades.Parroquia', verbose_name='Parroquia')),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='generalidades.Sector', verbose_name='Sector')),
                ('servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.Servicios', verbose_name='Servicio a Contratar')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='generalidades.Ubicacion', verbose_name='Ubicacion')),
                ('vivienda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='generalidades.Vivienda', verbose_name='Vivienda')),
            ],
            options={
                'verbose_name': 'Cliente a Contratar',
                'verbose_name_plural': 'Contratos Generados',
            },
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='contratado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contratos.Contratado'),
        ),
    ]
