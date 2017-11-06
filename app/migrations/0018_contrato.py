# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-06 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20171103_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limite_usuarios', models.IntegerField(default=0)),
                ('fecha_caducidad', models.DateField(blank=True, null=True)),
                ('creado', models.DateTimeField(editable=False)),
                ('modificado', models.DateTimeField(editable=False)),
            ],
        ),
    ]
