# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 13:20
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supervise', '0002_auto_20170227_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaofinterest',
            name='place',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326),
        ),
    ]
