# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-01 11:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20170823_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='esta_activo',
        ),
    ]
