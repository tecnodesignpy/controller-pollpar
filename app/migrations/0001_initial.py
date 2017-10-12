# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-01 20:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcacione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=200)),
                ('estado', models.CharField(blank=True, choices=[(0, 'Entrada'), (1, 'Salida')], max_length=40, null=True)),
                ('latitud', models.CharField(blank=True, max_length=200, null=True)),
                ('longitud', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.CharField(blank=True, max_length=200, null=True)),
                ('hora', models.CharField(blank=True, max_length=200, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='perfiles/avatar')),
                ('telefono', models.CharField(blank=True, max_length=40, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, max_length=40, null=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=40, null=True)),
                ('pais', models.CharField(blank=True, max_length=40, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=40, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
