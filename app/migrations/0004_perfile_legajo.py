# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-03 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170803_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfile',
            name='legajo',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
