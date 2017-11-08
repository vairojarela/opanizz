# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0002_auto_20170623_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_cancer',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Cancer'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_diabetes',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Diabetes'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_enfermedad_circulatorio',
            field=models.CharField(blank=True, choices=[('Trastorno en la presion arterial', 'Trastorno en la presion arterial '), ('Alteraciones cardiacas', 'Alteraciones cardiacas'), ('Angina de pecho', 'Angina de pecho '), ('Infarto de miocardio', 'Infarto de miocardio'), ('Otras enfermedades relacionados', 'Otras enfermedades relacionados:'), ('Ninguna', 'Ninguna')], help_text='Indique si Padece', max_length=50, verbose_name='Enfermedades Circulatorias'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_enfermedad_corazon',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Enfermedades del Corazon'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_enfermedad_digestivo',
            field=models.CharField(blank=True, choices=[('Enfermedades del higado', 'Enfermedades del higado'), ('Ulcera gastroduodenal', 'Ulcera gastroduodenal'), ('Dispepcia', 'Dispepcia'), ('Gastritis', 'Gastritis'), ('Otras enfermedades', 'Otras enfermedades'), ('Ninguna', 'Ninguna')], help_text='Indique si Padece', max_length=50, verbose_name='Enfermedades Digestivas'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_enfermedad_renal',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Enfermedades Renales'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_enfermedad_respiratoria',
            field=models.CharField(blank=True, choices=[('Bronquitis', 'Bronquitis Cronica'), ('Tuberculosis', 'Tuberculosis'), ('Asma', 'Asma'), ('Otras', 'Otras'), ('Ninguna', 'Ninguna')], help_text='Indique si Padece', max_length=50, verbose_name='Enfermedades Respiratorias'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_enfermedades_importantes',
            field=models.CharField(blank=True, max_length=250, verbose_name='Otras Importantes'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_enfermendad_mental',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Enfermedades Mentales'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_estatura',
            field=models.CharField(blank=True, max_length=7, verbose_name='Indique su Estatura'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_indique_circulatorio',
            field=models.CharField(blank=True, help_text='Especifique Enfermedad Circulatoria', max_length=150, verbose_name='Indique'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_indique_digestivo',
            field=models.CharField(blank=True, help_text='Especifique Enfermedad Digestiva', max_length=150, verbose_name='Indique'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_indique_otras',
            field=models.CharField(blank=True, help_text='Especifique la enfermedad', max_length=150, verbose_name='Indique'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_indique_respiratoria',
            field=models.CharField(blank=True, help_text='Especifique enfermedad Respirarotia', max_length=150, verbose_name='Indique'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_otras_enfermedades',
            field=models.CharField(blank=True, choices=[('Reumatismo', 'Reumatismo'), ('Artritis', 'Artritis'), ('Hemorragias de cualquier indole', 'Hemorragias de cualquier indole'), ('Perdida del conocimiento', 'Perdida del conocimiento'), ('Enfermedades en los huesos', 'Enfermedades en los huesos'), ('Convulsiones', 'Convulsiones'), ('Paralisis', 'Paralisis'), ('Ninguna', 'Ninguna')], help_text='Indique si Padece', max_length=50, verbose_name='Otras Enfermedades'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_peso',
            field=models.CharField(blank=True, max_length=7, verbose_name='Indique su peso'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_presion_arterial',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Presion Arterial Alta'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='beneficiario_salud',
            field=models.CharField(blank=True, choices=[('Buena', 'Buena'), ('Regular', 'Regular'), ('Mala', 'Mala')], max_length=7, verbose_name='Estado de Salud'),
        ),
        migrations.AlterField(
            model_name='contratado',
            name='cancer',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Cancer'),
        ),
        migrations.AlterField(
            model_name='contratado',
            name='diabetes',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Diabetes'),
        ),
        migrations.AlterField(
            model_name='contratado',
            name='enfermedad_corazon',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Enfermedades del Corazon'),
        ),
        migrations.AlterField(
            model_name='contratado',
            name='enfermedad_renal',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Enfermedades Renales'),
        ),
        migrations.AlterField(
            model_name='contratado',
            name='enfermendad_mental',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Enfermedades Mentales'),
        ),
        migrations.AlterField(
            model_name='contratado',
            name='indique_otras',
            field=models.CharField(blank=True, help_text='Especifique la enfermedad', max_length=150, verbose_name='Indique'),
        ),
        migrations.AlterField(
            model_name='contratado',
            name='presion_arterial',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Si', 'Si')], max_length=2, verbose_name='Presion Arterial Alta'),
        ),
        migrations.AlterField(
            model_name='contratado',
            name='punto_referencia',
            field=models.CharField(max_length=250, verbose_name='Punto de Referencia de busqueda'),
        ),
    ]
