# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-03 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20171103_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcacione',
            name='fecha',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
