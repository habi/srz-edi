# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0004_auto_20161019_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='osm_compare',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]