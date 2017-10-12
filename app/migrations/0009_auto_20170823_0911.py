# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 13:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_perfile_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono_id', models.CharField(blank=True, max_length=40, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=40, null=True)),
                ('legajo', models.CharField(blank=True, max_length=40, null=True)),
                ('esta_activo', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='perfile',
            old_name='activo',
            new_name='esta_activo',
        ),
    ]
