# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-23 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_marcacione_zona'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfile',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]
